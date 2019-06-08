while True:
    a = int(input('输入成绩:'))
    if 90 <= a <= 100:
        print('您的成绩为:A')
    elif 89 <= a <= 80:
        print('您的成绩为:B')
    elif 79 <= a <= 70:
        print('您的成绩为:C')
    elif 69 <= a <= 60:
        print('您的成绩为:D')
    elif 0 <= a < 60:
        print('您的成绩为:E')
    else:
        print('输入错误')
