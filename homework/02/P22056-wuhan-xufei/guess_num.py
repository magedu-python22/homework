#！/user/python3
#-*- codeing: utf-8 -*-
#@time   : 2019/6/6 23:03
#@AUthor : xifei!
#@FileName : guess_num.py
#@SoftWare : PyCharm

import random
n1 = random.randint(100,999)
n2 = int(input('输入你猜的三位数：'))
while 1:
    if n1 == n2:
        print('猜对啦')
        break
    elif n1 > n2:
        print('小了')
    else:
        print('大了')
    n2 = int(input('输入你再猜一个三位数：'))