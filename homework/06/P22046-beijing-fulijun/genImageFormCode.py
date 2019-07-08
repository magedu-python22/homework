#!/usr/bin/env python
# coding:utf-8
# @author: fulijun
# @date: 2019-07-06

'''
随机生成100个验证码，每个验证码由6个元素构成:
1 要求使用random模块
2 验证码由字母和数字构成
3 要求验证码中的每个元素为一种颜色
提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
demo:
Z (19, 157, 229)
2 (239, 10, 145)
Z (145, 142, 244)
M (231, 58, 7)
T (202, 19, 72)
F (182, 136, 237)
要求生成 png 或者jpg 格式的图片，关于如何生成图片 请搜索下python PIL生成图片
'''

import os
import random
import string
from PIL import Image, ImageDraw, ImageFont 

def colorGenerator():
    tinct = random.randint(0, 255)
    brightness = random.randint(0, 255)
    purity= random.randint(0, 255)
    
    # 返回随机生成的颜色色相、明度和纯度的值
    return tinct, brightness, purity

def authCodeGenerator():
    # 验证码由字母（包括大写和小写）和数字构成
    code_elements = string.ascii_letters + string.digits
    # 生成随机的验证码
    return random.choice(code_elements)

def buildAuthCodeImage(code_len, img_file):
    # 获取一个Image对象，参数分别是RGB模式。宽150，高30，随机颜色
    code_image = Image.new('RGB', (150,30), colorGenerator())
    # 获取一个画笔对象，将图片对象传过去
    code_draw = ImageDraw.Draw(code_image)
    # 获取一个font字体对象参数是ttf的字体文件的目录，以及字体的大小
    code_font = ImageFont.truetype('C:/Windows/Fonts/Arial.ttf', size=26)
    
    for i in range(code_len):
        # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
        code_draw.text((10+i*30, 0), authCodeGenerator(), colorGenerator(), font=code_font)
    
    # 将生成的验证码图片保存到png格式的图片文件
    code_image.save(open(img_file,'wb'),'png')
    
if __name__ == '__main__':
    image_file = os.path.join(os.curdir, 'authCode.png')
    buildAuthCodeImage(6, image_file)
    """
    这样保存的话，文件名字会不会有问题？
    """
