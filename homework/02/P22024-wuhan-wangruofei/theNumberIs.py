# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:50:31 2019

@author: YURiCA
"""

import random
num=random.randint(0,999)
while(1):
    inputNum=int(input("请输入一个数>>> "))
    if inputNum>num:
        print('大了！')
    elif inputNum<num:
        print('小了！')
    else:
        print('猜中了！')
        break


# break 后面多了分好，  inputNum=int(input("请继续输入>>> "))这句当道 if的上面试试
# ok 没有问题