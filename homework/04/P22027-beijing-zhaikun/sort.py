"""
【二：本周作业】请同学们于下周天晚上10点前，将作业上传至GitHub；
s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面

"""
s = "awFgWFWSAF12434861"
uper = ""
lower = ""
odd = ""
even = ""
for a in s:
    if a.islower():
        lower += a
    elif a.isupper():
        uper += a
    elif a.isdigit():
        if int(a) % 2 == 0:
            odd += a
        else:
            even += a
uperlst = list(uper)
uperlst.sort()
uper = "".join(uperlst)
lowerlst = list(lower)
lowerlst.sort()
lower = "".join(lowerlst)
oddlst = list(odd)
oddlst.sort()
odd = "".join(oddlst)
evenlst = list(even)
evenlst.sort()
even = "".join(evenlst)
#所有的小写字母在大写字母前面
print(lower+uper+even+odd)
