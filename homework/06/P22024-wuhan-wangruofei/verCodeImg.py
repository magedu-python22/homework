from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
import random
import string

def GetChar():
    """
    获取一个由大写字母和数字组成的字符串
    :return: 字符串
    """
    return random.choice(string.ascii_uppercase + string.digits)

def GetRandomColor():
    """
    获取一个随机颜色的RGB组合
    :return: (R, G, B)
    """
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def main():
    """
    生成图片
    :return:None
    """
    #设置底图参数，'RGB'模式，size是(200, 30)，颜色为黑色
    image = Image.new('RGB', (200, 30), (0, 0, 0))
    #获取画笔
    pen = ImageDraw.Draw(image)
    for i in range(6):
        random_char = GetChar()
        #绘图
        pen.text((15 + i * 30, random.randint(0, 10)), random_char, GetRandomColor(), ImageFont.truetype('simsun.ttc', 20))
    #保存图像
    image.save(open('Vercode.png', 'wb'), 'png')

if __name__ == '__main__':
    main()
