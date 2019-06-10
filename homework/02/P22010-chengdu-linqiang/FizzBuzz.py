for i in range(1,101):
    char= '\n' if i%10==0 else ','
    if i%3==0:
        print('FizzBuzz',end=char) if i%5==0 else print('Fizz',end=char)
    elif i%5==0:
        print('Buzz',end=char)
    else:
        print(i,end=char)


# 写的不错~