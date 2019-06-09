#!/usr/bin/env python
# -*- coding:utf-8 -*-

for i in range(0,101):
   if i == 0:
       print(i)
   elif i % 15 == 0:
   # if i % 3 == 0 and i % 5 == 0:
       print('FizzBuzz')
   elif i % 3 == 0:
       print('Fizz')
   elif i % 5 == 0:
       print('Buzz')
   else:
       print(i)