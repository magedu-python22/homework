# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:55:00 2019

@author: YURiCA
"""
l=[0]
for i in range(1,101):
    if i%3 and i%5:
        l.append(i)
    elif i%3 and (not i%5):
        l.append('Buzz')
    elif (not i%3) and i%5:
        l.append('Fizz')
    else:
        l.append('FizzBuzz')

print(l)
# 考虑下不换行？
# ok 没有问题