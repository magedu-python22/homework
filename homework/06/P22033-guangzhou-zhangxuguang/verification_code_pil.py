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
import random
import string
from PIL import Image, ImageDraw


n = 100  # 生成验证码数量

for i in range(n):
    # 随机生成6个字符串
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 6))
    # 生成一个颜色随机的大小为190,30的图片，用于保存验证码
    img = Image.new(mode="RGB", size=(190, 30), color=(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # 设置图片的绘制颜色
    draw = ImageDraw.Draw(img, "RGB")
    # 逐个字符绘制
    for j, code in enumerate(ran_str):
        # 通过draw.text方法，设置图片上字符串的x,y坐标，字符串，颜色，字体（for循环6次，生成6个字符的验证码)
        draw.text([10 + j * 30, 10], code, (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
    # 将6位验证码保存为png格式
    img.save("code"+str(i)+".png", "png")

"""
简洁~
"""

