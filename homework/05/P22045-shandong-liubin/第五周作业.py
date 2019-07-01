import random
c=[str(i) for i in range(10)]
a=[chr(i) for i in range(65,91)]
b=[chr(i) for i in range(97,123)]
lists=a+b+c

def color():#颜色函数
    colors=[]
    for i in range(3):
        i=random.randint(0,255)
        colors.append(i)
    return colors

def randomnum():
    return random.choice(lists)

def verification(much,len=6):
    muchs=[]
    for i in range(much):
        num=[]
        for i in range(len):
            i={randomnum():color()}
            num.append(i)
        muchs.append(num)
    return muchs

print(verification(100))