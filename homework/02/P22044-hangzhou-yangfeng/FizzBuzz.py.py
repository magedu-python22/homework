#!/usr/bin/env python
# coding: utf-8

n = 100
FizzBuzz = [0]
for i in range(1,n+1):
    if i % 3 == 0:    
        if i % 5 == 0:
            print('FizzBuzz')
            FizzBuzz.append('FizzBuzz')
        print('Fizz')
        FizzBuzz.append('Fizz')
    elif i % 5 == 0:
        print('Buzz')
        FizzBuzz.append('Buzz')
    else:
        print(i)
        FizzBuzz.append(i)
print(FizzBuzz)

