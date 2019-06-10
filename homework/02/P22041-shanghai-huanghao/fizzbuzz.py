l = [0] * 101
for i in range(0, 101):
	if i%3 != 0 and i%5 != 0:
		l[i] = str(i)
		continue
	elif i%3 == 0 and i%5 == 0:
		l[i] = 'FizzBuzz'
		continue
	elif i%3 == 0:
		l[i] = 'Fizz'
		continue
	else:
		l[i] = 'Buzz'
print(', '.join(l))

# 写的真好