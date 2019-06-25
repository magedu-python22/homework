# -*- coding: utf-8 -*-
# @file   : Sort.py
# @author : wfs
# @date   : 2019/06/23
# @version: 1.0
# @desc   : 字符串排序


"""
s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1. 所有的小写字母在大写字母前面
2. 所有的字母在数字前面
3. 所有的奇数在偶数前面

字符串判断 is系列

isalnum() -> bool 是否是字母和数字组成  isalpha() 是否是字母
isdecimal() 是否只包含十进制数字
isdigit() 是否全部数字(0~9)
isidentifier() 是不是字母和下划线开头，其他都是字母、数字、下划线  islower() 是否都是小写
isupper() 是否全部大写
islower() 是否都是小写
isspace() 是否只包含空白字符

"""
s = "9SorFt5ainNg12980637"

upper_list = []
lower_list = []
even_num = []
odd_num = []

for i in s:
    if i.isalpha():
        if i.islower():
            lower_list.append(i)
        else:
            upper_list.append(i)
    else:
        if int(i) % 2 == 0:
            even_num.append(i)
        else:
            odd_num.append(i)

lower_list.sort()
for x in (upper_list, odd_num, even_num):
    x.sort()
    lower_list.extend(x)
print("".join(lower_list))



"""
没有问题，写的很好
"""