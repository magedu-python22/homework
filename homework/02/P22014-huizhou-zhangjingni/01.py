#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/3 19:54

import random
answer = random.randint(0,999)
# print(answer)
while True:
    n = input('plz input an integer:')
    if n == ' ' or n == '':
        break
    else:
        n = int(n)
    if n == answer :
        print('congratulation')
        break
    flag = '>' if n > answer else '<'
    print('n {} answer'.format(flag) )

# 写的很好~

