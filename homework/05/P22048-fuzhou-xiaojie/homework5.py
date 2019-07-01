#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/6/29 9:15
# @Author  : xiaojie
# @Email   : 32904622@qq.com
# @File    : homework5.py
# @Software: PyCharm


'''随机生成100个验证码，每个验证码由6个元素构成:
1、要求使用random模块
2、验证码由字母和数字构成
3、要求验证码中的每个元素为一种颜色'''

import random
import string

n = 100
code_library = list(string.ascii_letters) + list(range(10))
code = [0] * n
code_color = [0] * 3

for i in range(n):
    code[i] = [0] * 6
    for j in range(6):
        code[i][j] = [0] * 2
        code[i][j][0] = random.choice(code_library)
        for k in range(3):
            code_color[k] = random.randint(0, 256)
        code[i][j][1] = tuple(code_color)
    print(i+1, code[i])


