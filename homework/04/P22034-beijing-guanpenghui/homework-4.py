#输入字符串，包含大小写字母和数字
s = input('pls input str:')
#定义空列表
slower = []
supper = []
sodd = []
seven = []
#执行循环，将每个字符放入对应的列表中
for x in s:
    if ord(x) >= 97:
        slower.append(x)
    elif ord(x) >= 65 and ord(x) <= 90:
        supper.append(x)
    elif int(x) % 2 != 0:
        sodd.append(x)
    else:
        seven.append(x)
print(slower+supper+sodd+seven)
"""
有些小问题：Sorting123456879AFLdfkgs 试试这个排序
"""