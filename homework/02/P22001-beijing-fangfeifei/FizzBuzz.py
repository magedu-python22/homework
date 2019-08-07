print(0)
for i in range(1,101):
    if(not i%3) & (not i%5):
        print('FizzBuzz')
    elif not i%3:
        print('Fizz')
    elif not i%5:
        print('Buzz')
    else:
         print(i)