'''
FizzBuzz
功能描述：遍历并打印0到100，如果数字能被3整除，显示Fizz；
		  如果数字能被5整除，显示Buzz；
          如果能同时被3和5整除，就显示FizzBuzz。
          结果应该类似：0,1,2，Fizz，4，Buzz，6……14，FizzBuzz，16……
'''
num = 0
for i in range(101):
	num = num+1
	if i%3 == 0 and i%5 != 0:
		print('Fizz ',end='')
	elif i%5 == 0 and i%3 != 0:
		print('Buzz ',end='')
	elif i%3 == 0 and i%5 == 0:
		print('FizzBuzz ',end='')
	else:
		print(i,end=' ')
	if num % 10 == 0:
		print()

# 逻辑上看着是没有问题的, 试试有没有更好的写法？

