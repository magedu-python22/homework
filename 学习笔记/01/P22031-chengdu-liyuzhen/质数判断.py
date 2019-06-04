while True:
    a = int(input('输入一个大于1的自然数:'))#假设5
    if a >= 1:
        for i in range(2, a):#[2,5]
            if a % i == 0:#1次5mod2余1 进不了if 2次5mod3余2 3次5mod4余1
                print('不是质数')
                break
        else:
            print('是质数')
    else:
        print('输入错误')
