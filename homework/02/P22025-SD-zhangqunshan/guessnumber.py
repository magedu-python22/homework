'''
猜数字
随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中
'''
import random
num = random.randint(1,1000)
print(num)
while True:
    guessnum = int(input("请输入一个三位数的数字："))
    if guessnum > num:
        print("你猜大了！")
    elif guessnum < num:
        print("你猜小了！")
    else:
        print("你猜对了！")
        break