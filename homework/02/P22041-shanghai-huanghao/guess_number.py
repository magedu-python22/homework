import random
n = random.randint(0, 999)
while True:
	m = int(input('>>>'))
	if m > n:
		print('too big')
		continue
	elif m < n:
		print('too small')
		continue
	else:
		print('Bingo')
		break

# 不用continue 试试