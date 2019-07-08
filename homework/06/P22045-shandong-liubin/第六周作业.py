import random
from PIL import Image,ImageDraw
def getrandomstr():
    random_char = random.choice([str(random.randint(0, 9)),
                                 chr(random.randint(97, 122)),
                                 chr(random.randint(65, 90))])
    return random_char
def getrandomcolor():
    random_list=[i for i in range(256)]
    return tuple(random.sample(random_list,k=3))
def newlmage():
    image=Image.new("RGB",(180,30),getrandomcolor())
    darw=ImageDraw.Draw(image)
    for i in range(6):
        randomchar=getrandomstr()
        darw.text((10+i*30,10),randomchar,getrandomcolor())
    return image.save(open("K:/secureCRT/text.png","wb"),'png')
newlmage()
"""
文件名一般都是变量的。别的是没有啥问题的
"""