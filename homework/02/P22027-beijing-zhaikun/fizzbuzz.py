print(0)
for a in range(1,100):
    if a%5 == 0 and a%3 == 0:
        a = "FizzBuzz"
    elif a%5 == 0 and (a%3 != 0):
        a = "Buzz"
    elif  a%3 == 0 and (a%5 != 0):
        a = "Fizz"
    print(a)

# 少个100哦