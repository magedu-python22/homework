'''
猜数字
功能描述：随机选择一个三位以内的数字作为答案。用户输入一个数字，程序会提示大了或是小了，直到用户猜中。
'''

import random

print('Game start.Please guest number.')

guestNum = random.randint(0, 1000)

while True:
	userInput = int(input('Please input number >>> '))
	if userInput == guestNum:
		print('You win! Game over.')
		break

	if userInput > guestNum:
		print('Bigger!')
	else:
		print('Smaller!')