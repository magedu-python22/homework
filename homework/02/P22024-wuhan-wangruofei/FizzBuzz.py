# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:55:00 2019

@author: YURiCA
"""
print(0)
for i in range(1,101):
    if i%3 and i%5:
        print(i)
    elif i%3 and (not i%5):
        print('Buzz')
        
    elif (not i%3) and i%5:
        print('Fizz')
    else:
        print('FizzBuzz')


# 考虑下不换行？