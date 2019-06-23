# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面

#借用快速排序的思想，进行分治
#先将字母和数字分开，然后分别对字母和数字排序
#字母和数字拆分
def Par_Letter_Number(List,low,high):
    pivot = List[low]
    while low < high:
        while (low < high) and (List[high].isdigit()):
            high -= 1
        List[low] = List[high]
        while (low < high) and (List[low].isalpha()):
            low += 1
        List[high] = List[low]
    List[low] = pivot
    return low



def Par_Upper_Lower(List,low,high):
    """
    大写字母和小写字母拆分
    :param List:
    :param low:
    :param high:
    :return:
    """
    pivot = List[low]
    while low < high:
        while (low < high) and (List[high].isupper()):
            high -= 1
        List[low] = List[high]
        while (low < high) and (List[low].islower()):
            low += 1
        List[high] = List[low]
    List[low] = pivot
    return low



def Par_Odd_Even(List,low,high):
    """
    奇数和偶数拆分
    :param List:
    :param low:
    :param high:
    :return:
    """
    pivot = List[low]
    while low < high:
        while (low < high) and (not int(List[high])&1):
            high -= 1
        List[low] = List[high]
        while (low < high) and (int(List[low])&1):
            low += 1
        List[high] = List[low]
    List[low] = pivot
    return low

def Par(List,low,high):
    """
    排序
    :param List:
    :param low:
    :param high:
    :return:
    """
    pivot = List[low]
    while low < high:
        while (low < high) and (pivot<List[high]):
            high -= 1
        List[low] = List[high]
        while (low < high) and (pivot>List[low]):
            low += 1
        List[high] = List[low]
    List[low] = pivot
    return low

def main():
    while True:
        string = input(">>> ")
        if string.isalnum():
            break
        else:
            print("字符串只能包括数字和字母")
    List = ' '.join(string).split(' ')
    low = 0
    high = len(string) - 1
    letter = Par_Letter_Number(List,low,high)
    lower = Par_Upper_Lower(List,low,letter)
    odd = Par_Odd_Even(List,letter+1,high)
    Par(List,low,lower)
    Par(List,lower+1,letter)
    Par(List,letter+1,odd)
    Par(List,odd+1,high)
    string1 = ''.join(List)
    print(string1)


if __name__ == '__main__':
    main()

    """
    1 元素里面也要排序下
    2 再看下这个代码哈
    3 注释参考下 Par_Odd_Even 里面的
    """