#!/usr/bin/env python
# -*- coding:utf-8 -*-

for i in range(0,101):
   if i == 0:
       print(i, end=' ')
   elif i % 15 == 0:
   # if i % 3 == 0 and i % 5 == 0:
       print('FizzBuzz', end=' ')
   elif i % 3 == 0:
       print('Fizz', end=' ')
   elif i % 5 == 0:
       print('Buzz', end=' ')
   else:
       print(i, end=' ')

# 不用换行输出试试？