import random
import string
from PIL import Image, ImageDraw, ImageFont, ImageFilter

# 随机数
def PIN():
    return random.choice(string.ascii_letters + string.digits)
# 颜色
def color():
    return (random.randint(0, 255) for _ in range(3))

# 设置图片大小，以像素为单位
w, h = 360, 65

# 构建image对象,(mode，size(二元组)，color)
image = Image.new('RGBA', (w, h), tuple(color()))

# 加载自定义字体，并创建字体对象
font = ImageFont.truetype('fonts/COOPBL.TTF', size=40)

# 创建draw对象
draw = ImageDraw.Draw(image, 'RGBA')

# 填充背景色
for x in range(w):
    for y in range(h):
        draw.point((x, y), fill=(225, 255, 255))

"""
显示验证码，并偏移显示位置
不会算法，偏移位置瞎整的，不超界就行了
"""
for code in range(6):
    draw.text((60*code+10, random.randint(-10, 20)), PIN(), font=font, fill=tuple(color()))

# 高斯模糊处理
image = image.filter(ImageFilter.GaussianBlur(2))
# 保存图片
image.save('PIN.png', 'png')