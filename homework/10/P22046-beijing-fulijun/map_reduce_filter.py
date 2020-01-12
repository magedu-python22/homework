#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'fulijun'
__date__ = '2020-01-12'

"""
简单用函数实现一下map，reduce，filter等函数
提示：
	map, reduce, filter一般都是接收两个参数(fn, Iterable)
要求：
	1、实现的函数返回结果时，可以不为惰性
	2、检测Iterable是否为可迭代对象，如果不可迭代，抛出异常”Iterable not is Iterable“
"""

from collections import Iterable

def map(fn, iterable):
    if not isinstance(iterable, Iterable):
        raise ValueError('Interable not is Iterable')
     
    for i in iterable:
        yield fn(i)

def fn(x):
    return x * x

ret = list(map(fn, [1,2,3,4,5,6,7,8,9]))
print(ret)
str1 = list(map(str, [1,2,3,4,5,6,7,8,9]))
print(str1)
   

def reduce(fn, iterable):
    if not isinstance(iterable, Iterable):
        raise ValueError('Interable not is Iterable')
    
    for i,val in enumerate(iterable):
        if i == 0:
            ret = val
            continue
        ret = fn(ret, val)
    return ret

def fn(x, y):
    return x + y

ret = reduce(fn, [1,3,5,7,9])   
print(ret)

def filter(fn, iterable):
    if not isinstance(iterable, Iterable):
        raise ValueError('Interable not is Iterable')
     
    for iter in iterable:
        if fn(iter):
            yield iter

def fn(n):
    return n % 2 == 1

ret = list(filter(fn, [1,2,4,5,6,9,10,15]))
print(ret)
