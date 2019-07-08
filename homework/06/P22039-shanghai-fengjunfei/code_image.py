"""
随机生成100个验证码，每个验证码由6个元素构成:
1、要求使用random模块
2、验证码由字母和数字构成
3、要求验证码中的每个元素为一种颜色
提示 颜色可以用数字来表示:一般都是3个 (0, 255)之间的数字来构成的
demo:
Z (19, 157, 229)
2 (239, 10, 145)
Z (145, 142, 244)
M (231, 58, 7)
T (202, 19, 72)
F (182, 136, 237)
"""

import random
import string
from PIL import Image,ImageFont,ImageDraw,ImageFilter

Colorset = set()
Colornum = 0
while Colornum < 7:
    Colorset.add(tuple(random.sample([x for x in range(256)],3)))
    Colornum = len(Colorset)

Strlst = random.sample(string.ascii_letters + string.digits,6)

Color = Colorset.pop()
image = Image.new('RGB',(90,20),Color)
font = ImageFont.truetype('/tmp/trapl.ttf')
draw = ImageDraw.Draw(image)

for i in range(6):
    Color = Colorset.pop()
    Str = Strlst.pop()
    draw.text((5+i*15,5),Str,Color)
    
image.save(open('/tmp/test.png','wb'),'png')

"""
注意保存文件的名字，最好是个变量
"""