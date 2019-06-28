#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/25 10:04
"""
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
"""
import random
import string
from PIL import Image, ImageDraw, ImageFont


# 生成随机字符 --> string
def code(stringset=(string.ascii_uppercase + string.ascii_lowercase + string.digits)):
    return random.choice(stringset)


# 生成颜色 --> tuple
def color():
    return tuple(random.randint(0,255) for _ in range(3))


# 生成验证码 --> list
def create_vcode(n=6):
    return list((code(),color()) for _ in range(n))


def create_image(n=1):
    image1 = Image.new('RGB', (200, 30*n), )
    draw1 = ImageDraw.Draw(image1)
    font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', size=26)  # 根据不同操作系统要修改
    for i in range(n):
        vcode = create_vcode()
        for j, c in enumerate(vcode):
            draw1.text((20 + j * 30, 30*i), c[0], c[1], font=font)
    image1.show()
    image1.save('code_image.jpg', 'jpeg')


create_image(100)




