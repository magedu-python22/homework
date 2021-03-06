#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'fulijun'
__date__ = '2019-07-29'

"""
comments = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]
第一版：我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度(10个字符)的评论用省略号替代,请写出 一个add_ellipsis 函数方法来实现
第二版:我们接到一个需求：有一个列表，里面装着很多用户评论，为了在页面正常展示，需要将所有超过一定长度的评论用省略号替代，如果有一天，我们拿到的评论不再是被继续装在列表里，而是在不可变的元组里呢？
请写出 一个add_ellipsis 函数方法来实现
"""

comments_list = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]

comments_tuple = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)

# 该函数可以分别或同时处理列表和元组
def add_ellipsis(*a_container, length=10):
    for item in a_container:
        if isinstance(item, (list, tuple)):
            for i in item:
                yield i[:length] + '......' if len(i) > length else i
        else:
            raise ValueError('list or tuple only !')
             
print('process list and tuple object')  
for comment in add_ellipsis(comments_list, comments_tuple):
    print(comment)

"""
这个题主要考查的是对yield 和raise 的用法
写的很好
"""