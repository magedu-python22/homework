import string
import random

#获取验证码列表（num个）
def getvcode(num):
    vcodelist = []
    while len(vcodelist)<num:
        vcode = random.sample(strlist, 6)
        num1 = 0
        num2 = 0
        for c in vcode:
            if c in number:
                num1 = num1 + 1
            else:
                num2 = num2 + 1
        if num1 > 0 and num2 > 0 and vcode not in vcodelist:
            vcodelist.append(vcode)
    return vcodelist

#获取颜色列表（num个）
def codecolor(num):
    coloralllist = []
    while len(coloralllist)<num:
        colorlist = []
        while len(colorlist) < 6:
            c1 = random.sample(range(256), 3)
            if c1 not in colorlist:
                colorlist.append(c1)
        if colorlist not in coloralllist:
            coloralllist.append(colorlist)
    return coloralllist

if __name__=="__main__":
    number = string.digits    #获取数字字符串
    capital = string.ascii_letters     #获取所有字母字符串（包含大小写）
    strlist = number+capital
    num = int(input("请输入需要生成的验证码的数量："))    #生成验证码的个数
    colorlist = codecolor(num)     #随机生成100个验证码颜色列表
    vcodelist = getvcode(num)      #随机生成100个验证码
    for v,c in zip(vcodelist, colorlist):  #将验证码与颜色结合
        sumlist = []
        for i,j in zip(v,c):
            sum = i+str(tuple(j))
            sumlist.append(sum)
        print(sumlist)
