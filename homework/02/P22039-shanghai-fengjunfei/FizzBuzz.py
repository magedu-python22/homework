ret = [0]
for i in range(1,101):
    if i % 15 == 0:
        ret.append('FizzBuzz')
    elif i % 3 == 0:
        ret.append('Fizz')
    elif i % 5 ==0:
        ret.append('Buzz')
    else:
        ret.append(i)

print(ret)
# ok 没有什么问题