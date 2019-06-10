import random
beguessed = random.randint(0,999)
while True:
    guessnum = int(input("请输入你要猜测的数字:"))
    if guessnum > beguessed:
        print("您输入的数字大了！！")
    elif guessnum < beguessed:
        print("您输入的数字小了！！！")
    else:
        print("恭喜你猜对了")
        break
# 逻辑上没有什么问题