#-*- comding:utf-8   -*-
# s = "Sorting1234"
# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面

i = 'asASDda1231fwe879s566dSDAwev'
resultlist = []
strlist = []
unevenlist = []
intlist = []

for s  in i:
    if s.islower():
        resultlist.append(s)
    elif s.isupper():
        strlist.append(s)
    elif int(s) % 2 == 0:
        intlist.append(s)
    else:
        unevenlist.append(s)
print(resultlist + strlist + unevenlist + intlist)