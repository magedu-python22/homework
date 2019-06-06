#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/4 20:05

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