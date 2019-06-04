#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/3 19:54

import random
answer = random.randint(0,99)
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


# FizzBuzz
dest = (0,'Fizz', 'Buzz', 'FizzBuzz')
for i in range(101):
    flag = 0
    if i > 0:
        if i % 3 == 0:
            flag += 1
        if i % 5 == 0:
            flag += 2
    if not flag:
        print(i)
    else:
        print(dest[flag])
