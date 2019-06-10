#get number
from random import randint
ansnumber = randint(0,999)
print('The answernumber is',ansnumber)
#compare number
while True:
    gusnumber = int(input('Pls input a number to compare:'))
    if gusnumber > ansnumber:
        print('You input number is larger than ansnumber,pls input again')
        continue
    elif gusnumber < ansnumber:
        print('You input number is smaller than ansnumber,pls input again')
        continue
    else:
        print('Congratuation,the number you input is right')
        break

# 不用continue的