import random
num=random.randint(0,999)

while True:
    input_num = int(input("Plz enter a num:"))
    if input_num > num:
        print('The number is bigger')
    elif input_num < num:
        print('The number is smaller')
    else:
        print('You guessed it.')
        break