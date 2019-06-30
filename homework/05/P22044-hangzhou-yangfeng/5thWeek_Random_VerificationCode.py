#!/usr/bin/env python
# coding: utf-8

# In[18]:


from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import random

#设定验证码中单个字符随机颜色
def getRandomColor():
    c1 = random.randint(0,255)
    c2 = random.randint(0,255)
    c3 = random.randint(0,255)
    return (c1,c2,c3)

#设定验证码中单个随机字符范围
def getRandomStr():
    random_num = str(random.randint(0,9))
    random_low_alpha = chr(random.randint(97, 122))
    random_upper_alpha = chr(random.randint(65, 90))
    random_char = random.choice([random_num, random_low_alpha,random_upper_alpha])
    return random_char

def getchecknum(num):

    for i in range(num):
              
        #设定图片尺寸宽高和背景色
        image = Image.new('RGB',(220,50),'white')
        #image = Image.new('RGB',(180,30),getRandomColor())

        #生成图片，设置图片中字体类型和大小
        draw = ImageDraw.Draw(image)
        font = ImageFont.truetype("font/IMPRTSHOW.TTF",size=30)
        #font = ImageFont.truetype("font/COLONNA.TTF",size=30)
        #font = ImageFont.truetype("font/STCAIYUN.TTF",size=30)

        #生成6个随机字符，定位绘图并附加随机颜色。
        for j in range(6):
            random_char = getRandomStr()
            draw.text((15+j*35, 0),random_char, getRandomColor(), font=font)
            
        #保存图片格式为png格式 
        f = 'png' + str(i) + '.' + 'png'

#       #使用jpg格式保存之前必须安装matplotlib
#         f = 'jpg' + str(i) + '.' + 'jpg'
        image.save(f)
        
    return f

getchecknum(3)


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




