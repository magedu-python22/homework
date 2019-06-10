import random as t
a=t.randint(0,999)
n=int(input('Please guess a number:'))
while True:
    if n==a:
        print('Bingo!You are right.')
        break
    elif n>a:
        print('You guess big.')
        n=int(input('Please guess a number again:'))
    else:
        print('You guess small.')
        n=int(input('Please guess a number again:'))

# 试试用下flag？  n=int(input('Please guess a number again:')) 这句放在 if 的上面试试？