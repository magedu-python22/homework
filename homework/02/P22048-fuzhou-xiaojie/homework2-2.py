#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/4 0:17
# @Author  : xiaojie
# @Email   : 32904622@qq.com
# @File    : homework2-2.py
# @Software: PyCharm


#FizzBuzz

for i in range(0, 101):
    if i == 0:
        print(i)
    elif i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 可以再优化下？