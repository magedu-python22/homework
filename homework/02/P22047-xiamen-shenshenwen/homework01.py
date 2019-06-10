#!/usr/bin/env python

import random

result = int(str(random.randrange(0, 1000)).lstrip('0'))
num = int(input('Please enter a number: ').strip().lstrip('0'))

while not num == result:
    if num > result:
        print('猜错啦，比答案大哦')
    if num < result:
        print('猜错啦，比答案小哦')
    num = int(input('Please enter a number: ').strip().lstrip('0'))

print(f"\n恭喜，猜中啦!!! 答案是：{result}")

# 这样写也行