'''
猜数字
功能描述：随机选择一个三位以内的数字作为答案。
用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
'''
import random

num = random.randint(0,999)

flag = True
while flag:
	guessnumber = int(input("请输入一个三位以内的数字："))
	if guessnumber == num:
		print("恭喜恭喜，猜对啦！")
		flag = False
	elif guessnumber < num:
		print("小啦小啦，请输入一个较大的数字")
	else:
		print("大啦大啦，请输入一个较小的数字")
