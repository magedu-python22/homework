#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random
num = random.randint(1,100)


Flag = True
while Flag:
    try:
        val = input('请输入一个两位数:')
        while len(val) >= 3:
            val = input('请输入一个两位数:')
        val = int(val)
        if val > num:
            print("biger")
        elif val < num:
            print('smaller')
        else:
            print('right')
            Flag = False
    except Exception as e:
        print(e)

