"""
s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面

"""

s = "So56rT12358955ing645873165dfadsa"
upstr = []
lowstr = []
odd = []
even = []

for i in s:
    if i.isupper():
        upstr.append(i)
    elif i.islower():
        lowstr.append(i)
    elif i.isdigit():
        if int(i)%2 != 0:
            odd.append(i)
        else:
            even.append(i)
sorting = upstr + lowstr + odd + even
for j in sorting:
    print(j, end='')
