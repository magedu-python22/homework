#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/19 10:19

# 给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
# 1 所有的小写字母在大写字母前面
# 2 所有的字母在数字前面
# 3 所有的奇数在偶数前面

s = "Sorting1234"
lower = []
upper = []
odd = []
even = []
for c in s:
    if c.islower():
        lower.append(c)
    elif c.isupper():
        upper.append(c)
    elif c.isdigit():
        if int(c) & 1 == 1:
            odd.append(c)
        else:
            even.append(c)

dest = ''.join(sorted(lower) + sorted(upper) + sorted(odd) + sorted(even))
print(dest)

"""
ok 写的很好~
"""