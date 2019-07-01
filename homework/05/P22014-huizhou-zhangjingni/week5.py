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
import platform
from PIL import Image, ImageDraw, ImageFont


# 生成随机字符 --> string
def vcode(stringset=(string.ascii_uppercase + string.ascii_lowercase + string.digits)):
    return random.choice(stringset)


# 生成颜色 --> tuple
def color():
    return tuple(random.randint(0,255) for _ in range(3))


def create_image(n=1,code=6):
    width = 30*code + 20
    height = 30*n
    image1 = Image.new('RGB', (width, height), )
    draw1 = ImageDraw.Draw(image1)
    # 不同操作系统字体路径不同
    os = platform.system()
    if os == 'Windows':
        font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', size=26)
    elif os == 'Linux':
        font = ImageFont.truetype('/usr/share/fonts/arial.ttf', size=26)
    else:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=26)
    for i in range(n):
        for j in range(code):
            draw1.text((15 + j * 30, 30*i), vcode(), color(), font=font)
    image1.show()
    image1.save('code_image.jpg', 'jpeg')


create_image(100)


