import string
import random
strall = string.ascii_letters + string.digits
vercode = []
#vercol = {}
for y in range(5):
    x = random.choice(strall) +  random.choice(strall) +  random.choice(strall) +  random.choice(strall) +  random.choice(strall) +  random.choice(strall)
    vercode.append([x])
print('生成的验证码如下：',vercode)
print()
for str1 in vercode:
    print('验证码{}中每个元素的颜色'.format(str1))
    b = str1[0]
    for c in b:
        color = []
        print(c,end=' ')
        for d in range(3):
            color.append(random.randint(0,255))
        print(color)
    print()

"""
考虑下颜色的显示，参考P22012-beijing-liyinkai
写成函数试试
"""
