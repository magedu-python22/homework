#-*- comding:utf-8   -*-
# P22第六周（7.1-7.7）学习安排及作业内容：
# 请同学们至少完成腾讯课堂如下学习章节：
# 【一：章节学习】
# 第17节  Python高阶函数与装饰器：
#         01-高阶函数和柯里化；
#         02-无参装饰器；
#         03-带参装饰器；
# 第18节  Python类型注解和functools模块：
#         01-类型注解；
#         02-functools之reduce和偏函数；
#         03-lru_cache；
# 第19节  函数综合习题讲解：
#         01-字典扁平化和base64编码实现；
#         02-求最大公共子串；
#         03-装饰器习题cache和命令分发器实现；
# 【二：本周作业】请同学们于下周天晚上10点前，将作业上传至GitHub；
# 随机生成100个验证码，每个验证码由6个元素构成:
# 1 要求使用random模块
# 2 验证码由字母和数字构成
# 3 要求验证码中的每个元素为一种颜色
# 提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
# demo:
# Z (19, 157, 229)
# 2 (239, 10, 145)
# Z (145, 142, 244)
# M (231, 58, 7)
# T (202, 19, 72)
# F (182, 136, 237)
# 要求生成 png 或者jpg 格式的图片，关于如何生成图片 请搜索下python PIL生成图片

#生成验证码
from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random

# 随机字母数字:
def rndChar():
    return random.choice([chr(random.randint(65,90)), str(random.randint(0,9))])
# 随机颜色1:
def rndColor():
    # return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    return (240, 200, 5)
# 随机颜色2:
def rndColor2():
    return (random.randint(0, 127), random.randint(0, 127), random.randint(0, 127))

# 240 x 60:
width = 240
height = 60
image = Image.new('RGB', (width, height), (255, 255, 255))
# 创建Font对象:
font = ImageFont.truetype(r'C:\Windows\Fonts\Arial.ttf', 36)
# 创建Draw对象:
draw = ImageDraw.Draw(image)
# 填充每个像素:
for x in range(width):
    for y in range(height):
        draw.point((x, y), fill=rndColor())
# 输出文字:
for t in range(6):
    draw.text((60 * t + 15, 10), rndChar(), font=font, fill=rndColor2())
# 模糊:
image = image.filter(ImageFilter.BLUR)
#保存当前路径
image.save('code.jpg', 'jpeg')

#图像缩放操作
def k75():
    # 打开一个jpg图像文件，注意是当前路径:
    im = Image.open('test.jpg')
    # 获得图像尺寸:
    w, h = im.size
    print('Original image size: %sx%s' % (w, h))
    # 缩放到50%:
    im.thumbnail((w//2, h//2))
    print('Resize image to: %sx%s' % (w//2, h//2))
    # 把缩放后的图像用jpeg格式保存:
    im.save('thumbnail.jpg', 'jpeg')












