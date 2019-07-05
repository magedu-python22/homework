# -*- coding: utf-8 -*-
# @file   : PIL_homework.py
# @author : wfs
# @date   : 2019/07/05
# @version: 1.0
# @desc   :

"""
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
"""



from PIL import Image
from PIL import ImageDraw
import random

# 获取一个随机颜色(r,g,b)格式的
def getRandomColor():
    c1 = random.randint(0, 255)
    c2 = random.randint(0, 255)
    c3 = random.randint(0, 255)
    return c1, c2, c3


# 获取一个随机字符串，每个字符串的颜色也是随机的
def getRandomStr():
    random_num = str(random.randint(0, 9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upoer_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha, random_upoer_alpha])

    return random_char


# 获取图片对象函数
def getImage(color, rgb='RGB', size=(180, 20)):
    return Image.new(rgb, size, color)


# 获取图片验证码对象函数
def getVeriCode():
    for i in range(6):
        # 随机获取6个字符
        random_char = getRandomStr()
        # 在图片上依次写入得到的字符，并附带上字符的颜色.参数是：定位，字符串，颜色
        draw.text((10 + i * 30, 0), random_char, getRandomColor())


# 获取一个image对象
sourceImage = getImage(getRandomColor())

# 获取一个画笔，并将image对象传给画笔
draw = ImageDraw.Draw(sourceImage)

# 调用生成图片验证码函数
getVeriCode()

# 保存图片到磁盘并命名
sourceImage.save(open('homework06.png', 'wb'), 'png')


