#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/10 18:26
# @Author  : xiaojie
# @Email   : 32904622@qq.com
# @File    : homework2-2.py
# @Software: PyCharm


''' FizzBuzz '''

print('0', end='. ')
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            print('FizzBuzz', end='. ')
        elif i % 3 == 0:
            print('Fizz', end='. ')
        else:
            print('Buzz', end='. ')
    else:
        print(i, end='. ')

# # ok 没有问题