print(0)
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print('FizzBizz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Bizz')
    else:
        print(i)
# 能否不换行输出呢？