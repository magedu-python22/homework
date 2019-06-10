#！/user/python3
#-*- codeing: utf-8 -*-
#@time   : 2019/6/7 8:09
#@AUthor : xifei!
#@FileName : FizzBuzz.py
#@SoftWare : PyCharm

for i in range(0,101):
    if i == 0:
        print(i)
    elif i % 3 == 0:
        if i % 5 == 0:
            print('FizzBuzz')
        else:
            print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)

# 不要换行试试了？