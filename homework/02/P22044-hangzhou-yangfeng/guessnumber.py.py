#!/usr/bin/env python
# coding: utf-8
import random
n = random.randint(0,999)
while True:
    m = int(input('>>>'))
    if m > n:
        print('big')
        continue
    elif m < n:
        print('small')
        continue
    else:
        print('Right')
        break




# 不用 continue 试试

可以，不用continue效果一样