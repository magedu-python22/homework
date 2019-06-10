import random

num = random.randint(0,999) #前后都是闭区间
prompt = 'please input a number between 0 and 999: '

while True:
	num1 = int(input(prompt).strip())
	if num1 > num:
		print('bigger')
	elif num1 < num:
		print('smaller')
	else:
		print('correct')
		break
	
# 没有毛病