import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 随机数
def PIN():
    return random.choice(string.ascii_letters + string.digits)
# 颜色
def color():
    return (random.randint(0, 255) for _ in range(3))

def PIN_convert(mode='RGBA', width=360, height=65):
    # 构建image对象,(色彩类型，size(二元组)，color)
    image = Image.new(mode, (width, height), tuple(color()))

    # 加载自定义字体，并创建字体对象
    font = ImageFont.truetype('fonts/COOPBL.TTF', size=40)

    # 创建draw对象
    draw = ImageDraw.Draw(image, mode)

    # 填充背景色
    for x in range(width):
        for y in range(height):
            draw.point((x, y), fill=(225, 255, 255))

    for code in range(6):
        draw.text((60*code+10, random.randint(-10, 20)), PIN(), font=font, fill=tuple(color()))
    """
    显示验证码，并偏移显示位置
    不会算法，偏移位置瞎整的，不超界就行了
    """
    # 返回高斯模糊处理
    return image.filter(ImageFilter.GaussianBlur())

for n in range(1,100):
    # 保存图片
    f = f'images/PIN_{n:0>3d}.png'
    PIN_convert().save(f, 'png')

"""
参考下P22012 同学的代码，虽然你写的也没有啥问题
"""