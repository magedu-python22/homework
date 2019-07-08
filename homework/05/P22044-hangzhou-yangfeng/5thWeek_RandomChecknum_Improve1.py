#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#生成随机验证码改进1
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

def checknum(num):
    """
    这样写注释
    :param num:
    :return:
    """
    for i in range(num):
        #设定图片尺寸宽高和背景色
        image = Image.new('RGB',(220,50),'white')
        #生成图片，设置图片中字体类型和大小
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("font/IMPRTSHOW.TTF",size=30)
        #生成6个随机字符，定位绘图并附加随机颜色
        for j in range(6):
            Rcolor = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
            Rstr = random.choice([str(random.randint(0,9)), chr(random.randint(65, 90)), chr(random.randint(97, 122))])
            draw.text((15+j*35, 0),Rstr,Rcolor, font=font)
        #保存图片格式为png格式 
        f = 'png' + str(i) + '.' + 'png'
        image.save(f)
    return f

checknum(3)


"""
很好~
"""