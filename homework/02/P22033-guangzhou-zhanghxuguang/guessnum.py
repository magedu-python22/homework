import random

rdnum = random.randint(0,1000)
while True:
    str = input("请输入您要猜的数：").strip().lstrip("0")
    if str.isdecimal():
        num = int(str)
        if num == rdnum:
            print("恭喜你，猜对了",end='，')
            break
        elif num > rdnum:
            print("猜大了，重新输入",end='，')
        else:
            print("猜小了，重新输入",end='，')
    else:
        print("非法输入",end='，')

# 不错，加了数字验证