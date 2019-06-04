# -*- coding: utf-8 -*-
"""
Created on Mon Jun  3 16:50:31 2019

@author: YURiCA
"""
#自定义一个数256，请用户输入，当小于256时提示小了，大于256时提示大了，直至用户输入等于256
import random
num=random.randint(0,999)
inputNum=int(input("请输入一个数>>> "))
while(1):
    if inputNum>num:
        print('大了！')
        inputNum=int(input("请继续输入>>> "))
    elif inputNum<num:
        print('小了！')
        inputNum=int(input("请继续输入>>> "))
    else:
        print('猜中了！')
        break;