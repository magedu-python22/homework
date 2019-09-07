#!/usr/bin/env python
#_*_coding:utf-8_*_
__author__ = 'fulijun'
__date__ = '2019-09-07'

"""
1. 请设计一个decorator，它可作用于任何函数上，并打印该函数的执行时间
"""

import datetime

def decorator(func):
    def wrapper(*args, **kwargs):
        time_rst = datetime.datetime.now()
        ret = func(*args, **kwargs)
        time_cur = datetime.datetime.now()
        print('function {} took {}s'.format(func.__name__, (time_cur - time_rst).total_seconds()))
        return ret
    return wrapper

@decorator
def dstportIncr(port, step, cnt):
    dst_ports = []
    for _ in range(int(cnt)):
        port %= 65536
        dst_ports.append(port)
        port += step
    return dst_ports
        
print(dstportIncr(80, 2, 10000))

"""
2. 请设计一个decorator，它可作用于任何函数上，要求可以接受一个int作为参数，如果该函数的执行时间大于int传递的时间话，请打印改函数名字和执行时间
"""
def timer_set(timer):
    try:
        timer = int(timer)
    except ValueError as err:
        print('args err {}'.format(err))
    return timer

def decorator(duration, func=lambda x:int(x)):
    def _decorator(fn):
        def wrapper(*args, **kwargs):
            time_rst = datetime.datetime.now()
            ret = fn(*args, **kwargs)
            delta = (datetime.datetime.now() - time_rst).total_seconds()
            print(type(delta), delta)
            if delta > func(duration):
                print('function {} took {}s, exceeded the threshold {}'.format(fn.__name__, delta, duration))
            return ret
        return wrapper
    return _decorator

# @decorator('1')
@decorator('1', timer_set)
def dstportIncr(port, step, cnt):
    dst_ports = []
    for _ in range(int(cnt)):
        port %= 65536
        dst_ports.append(port)
        port += step
    return dst_ports
        
print(dstportIncr(80, 2, 50000))

