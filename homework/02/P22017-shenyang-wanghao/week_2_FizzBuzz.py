
for number in range(0, 101, 1):
	if int(number) % 15 == 0 and int(number) > 0:
		number = 'FizzBuzz'
	elif int(number) % 3 == 0 and int(number) > 0:
		number = 'Fizz'
	elif number % 5 == 0 and int(number) > 0:
		number = 'Buzz'
	
	print(number)

	
# 考虑下不换行？