#!/usr/bin/env python
#
import random

def inputVerify(input):
    try:
        num = int(get_input)
        if 0 <= num <= 999:
            return num
        else:
            return -1
    except ValueError:
        return -2
    
answer = random.randint(0,999)
#print(answer)
while True:
    get_input = raw_input('Guess a number: [0-999]:')
    input_chk = inputVerify(get_input)
    if input_chk == -1:
        print('Wrong number, range 0-999, try again!')
    elif input_chk == -2:
        print('You have to input a number, try again!')
    else:
        if input_chk == answer:
            print('Congratulations!, guess right')
            break
        elif input_chk < answer:
            print('Too small, try again!')
        else:
            print('Too big, try again!')