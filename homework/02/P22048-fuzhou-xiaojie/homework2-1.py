#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 0:01
# @Author  : xiaojie
# @Email   : 32904622@qq.com
# @File    : homework2-1.py
# @Software: PyCharm


#  猜数字
import random

answer = random.randint(1, 1000)
for i in range(1000):
    num = int(input('输入一个小于100的数：'))
    if num != answer:
        if num > answer:
            print('比答案大了一点')
        else:
            print('比答案小了一点')
    else:
        print('答对了')
        break
