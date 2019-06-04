
print(0,end=',')
for i in range(1,101):
    if not i%3:
        i = "Fizz"
    elif not i%5:
        i = "Buzz"
    elif not i%15:
        i = "FizzBuzz"
    print(i,end=",")
