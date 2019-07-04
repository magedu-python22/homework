#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/7/4 10:34
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
    width = 40*code + 20
    height = 40*n
    image1 = Image.new('RGB', (width, height))
    draw1 = ImageDraw.Draw(image1)

    # 不同操作系统字体路径不同
    os = platform.system()
    if os == 'Windows':
        font = ImageFont.truetype(r'C:\Windows\Fonts\arial.ttf', size=36)
    elif os == 'Linux':
        font = ImageFont.truetype('/usr/share/fonts/arial.ttf', size=36)
    else:
        font = ImageFont.truetype('/Library/Fonts/Arial.ttf', size=36)
    for i in range(n):
        for j in range(code):
            draw1.text((15 + j * 40, 40*i), vcode(), color(), font=font)
    image1.show()
    image1.save('code_image.jpg', 'jpeg')


create_image(100)

