#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @file   : FizzBuzz.py
# @author : cjg
# @date   : 2019/06/10
# @version: 1.0
# @desc   : 按要求打印出相应的数字

"""
功能描述：遍历并打印0～100，如果数字能被3整除，显示Fizz；如果数字能被5整除，显示Buzz；如果能
同时被3和5整除，就显示FizzBuzz。结果应该类似: 0,1,2,Fizz,4,Buzz,6...14,FizzBuzz,16...
"""

for i in range(101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 5 == 0:
        print("Buzz")
    elif i % 3 == 0:
        print("Fizz")
    else:
        print(i)


# 没有什么问题