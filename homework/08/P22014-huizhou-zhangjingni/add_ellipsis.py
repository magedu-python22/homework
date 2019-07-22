#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/7/15 18:12
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


comments1 = [
    "Implementation note",
    "Changed",
    "ABC for generator",
]

comments2 = (
    "Implementation note",
    "Changed",
    "ABC for generator",
)


# 就地修改
def add_ellipsis_1(comments: list) -> list:
    for i, item in enumerate(comments):
        if len(item) > 10:
            comments[i] = '...'

    return comments


# 生成新列表
def add_ellipsis_2(comments) -> list:
    dest = []
    for item in comments:
        if len(item)>10:
            dest.append('...')
        else:
            dest.append(item)
    return dest


print(add_ellipsis_1(comments1))
print(add_ellipsis_2(comments2))

"""
可能是我没有说清楚，超过部分用.....表示
"""