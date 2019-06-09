import random
i = random.randint(0,100)
a = int(input('>>>'))
while a != i:
    if a > i:
        print('big than i')
    elif a < i:
        print('less than i')
    else:
        break
    a = int(input('>>>'))
print('guess right')