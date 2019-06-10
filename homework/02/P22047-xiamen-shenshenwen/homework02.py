#!/usr/bin/env python

for n in range(101):
    if n == 0:
        print(n, end=", ")
    elif n == 100:
        print('Buzz')
    else:
        if n % 3 == 0 and n % 5 == 0:
            print('FizzBuzz', end=", ")
        elif n % 5 == 0:
            print('Buzz', end=", ")
        elif n % 3 == 0:
            print('Fizz', end=", ")
        else:
            print(n, end=", ")

# 逻辑有点多，再想想