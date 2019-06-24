#!/usr/bin/env python

"""
s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面
"""

s = 'Sorting1234'
upper = ''
lower = ''
odd = ''
even = ''

for i in s:
    if i.isupper():
        upper = upper + i
    elif i.islower():
        lower = lower + i
    elif i.isdigit():
        if int(i) % 2 == 0:
            odd = odd + i
        else:
            even = even + i

lower.split().sort()
upper.split().sort()
print(f'{lower}{upper}{even}{odd}')

"""
元素里面也要排序下
"""