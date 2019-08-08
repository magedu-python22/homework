# -*- coding:utf-8 -*-
# @Time    : 2019/8/7 10:57
# @Author  : FANG FEIFEI 
# @FileName: strSort.py
# @Software: PyCharm

'''
s = "Sorting1234"
给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
1 所有的小写字母在大写字母前面
2 所有的字母在数字前面
3 所有的奇数在偶数前面
'''
def strSort(string):
    lower_str_list = []
    upper_str_list = []
    odd_int_list = []
    even_int_list = []
    result = ''
    for s in string:
        if ord(s) in range(48, 58):
            if int(s) % 2 == 0 :
                even_int_list.append(s)
            else:
                odd_int_list.append(s)
        elif ord(s) in range(65, 91):
            upper_str_list.append(s)
        elif ord(s) in range(97, 123):
            lower_str_list.append(s)

    return result.join(lower_str_list + upper_str_list + odd_int_list + even_int_list)

print(strSort("Sorting1234"))
"""
还有更好的写法，可以看下别的小伙伴的
"""

