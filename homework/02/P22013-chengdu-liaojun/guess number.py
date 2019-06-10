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

# 感觉a != i 这个是不是可以换种方法呢？