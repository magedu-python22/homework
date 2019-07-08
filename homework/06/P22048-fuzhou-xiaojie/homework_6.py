#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Time    : 2019/7/6 19:36
# @Author  : xiaojie
# @Email   : 32904622@qq.com
# @File    : homework_6.py
# @Software: PyCharm

from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random



def getRandomColor():
    '''获取一个随机颜色(r,g,b)格式的'''
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return (c1, c2, c3)

def getRandomStr():
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
    return random_char

for j in range(100):
    image = Image.new('RGB', (200, 30), 'white')
    draw = ImageDraw.Draw(image)
    Font2 = ImageFont.truetype("C:\Windows\Fonts\simsun.ttc", 30, index=0)
    for i in range(6):
        random_char = getRandomStr()
        # 在图片上一次写入得到的随机字符串,参数是：定位，字符串，颜色，字体
        '''
        这一句不知道是什么意思，  参数看不懂
        '''
        draw.text((10 + i * 30, 0), random_char, getRandomColor(), font=Font2)
# 保存到硬盘，名为test.png格式为png的图片
    image.save(open('test{}.png'.format(j), 'wb'), 'png')


"""
是draw.text的这个方法吧，里面要求你传入正确的参数后，才能调用，就是和你写函数方法差不多
"""