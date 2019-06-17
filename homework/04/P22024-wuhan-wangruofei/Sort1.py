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
for i in range(len(string)):
    if string[i].islower():
        List.insert(low,string[i])
        low += 1
        up += 1
        odd += 1
        even += 1
    elif string[i].isupper():
        List.insert(up,string[i])
        up += 1
        odd += 1
        even += 1
    elif string[i].isdigit() and int(string[i])&2:
        List.insert(odd,string[i])
        odd += 1
        even += 1
    else:
        List.insert(even, string[i])
        even += 1

s=''.join(List)
print(s)
