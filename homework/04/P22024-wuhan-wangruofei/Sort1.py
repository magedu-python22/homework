# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面
while True:
    string = input(">>> ")
    if string.isalnum():
        break
    else:
        print("字符串只能包括数字和字母")

List=[]
up=0
low=0
odd=0
even=0
for i in string:
    if i.islower():
        List.insert(low,i)
        low += 1
        up += 1
        odd += 1
        even += 1
    elif i.isupper():
        List.insert(up,i)
        up += 1
        odd += 1
        even += 1
    elif i.isdigit() and int(i)&1:
        List.insert(odd,i)
        odd += 1
        even += 1
    else:
        List.insert(even, i)
        even += 1

s=''.join(List)
print(s)

"""
元素里面也要排序下
"""