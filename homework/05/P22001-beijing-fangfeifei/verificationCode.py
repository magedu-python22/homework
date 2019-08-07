# -*- coding:utf-8 -*-
# @Time    : 2019/8/7 11:49
# @Author  : FANG FEIFEI 
# @FileName: verificationCode.py
# @Software: PyCharm
'''
随机生成100个验证码，每个验证码由6个元素构成:
1、要求使用random模块
2、验证码由字母和数字构成
3、要求验证码中的每个元素为一种颜色
提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
demo:
Z (19, 157, 229)
2 (239, 10, 145)
Z (145, 142, 244)
M (231, 58, 7)
T (202, 19, 72)
F (182, 136, 237)
'''
import random

def getRandomChr():
    num = random.randint(48,90)
    while num>= 58 and num<= 64:
        num = random.randint(48,90)
    return chr(num)

def getVCodes() :
    vcode_list = []
    for i in range(0,6):
        vcode_list.append(getRandomChr())
    return vcode_list

def getVColors() :
    vcolor_list = []
    for i in range(0,6):
        vcolor_list.append(random.sample(range(256), 3))
    return vcolor_list


def getVerificationCode(num):
    rcode_list = []
    for i in range(0,num):
        vcode_list = getVCodes()
        vcolor_list = getVColors()
        rcode = []
        for code, color in zip(vcode_list, vcolor_list):
            rcode.append(code+str(tuple(color)))
        rcode_list.append(rcode)
    return rcode_list

print(getVerificationCode(10))