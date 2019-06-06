#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/5/27 15:53

#1.给一个半径，求圆的面积和周长
radius = float(input('plz input radius'))
print('area=' + str(3.14 * radius * radius))
print('circumference=' + str(3.14 * 2 * radius))

#2.输入两个数，比较大小后，从小到大升序打印
num1 = input('plz input num1')
num2 = input('plz input num2')
if num1 >= num2:
    print(num2, num1)
else:
    print(num1, num2)

#3.判断学生成绩，成绩等级A~E。其中，90分以上为'A'，80~89分为'B'，70~79分为'C'，60~69分为'D'，60分以下为'E'
score = float(input("plz input score"))
if score >= 90:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
elif score >= 60:
    print('D')
else:
    print('E')

#4.死循环输入数字，输入后打印出之前输入的最大值和之前所有数字的平均数，如果输入的不是数字，而是quit字符串或者空格，则结束循环，退出程序
count = 1
sum1 = 0
while True:
    number = input('plz input number')
    if number == '' or number == 'quit' or number == ' ':
        break
    sum1 += int(number)
    print(int(sum1) / count)
    count += 1

#5.用 * 打印一个边长为 n 的正方形，n 为整数
n = 3
for i in range(n):
    print(' *'*n)

#6.输入一个正整数n，求0到这个数以内的所有 奇数的和 与 偶数的和
n = int(input("plz input number"))
sum_odd = 0
sum_even = 0
for i in range(1,n+1):
    if i & 1:
        sum_odd += i
    else:
        sum_even += i
print("奇数的和：{}，偶数的和：{}".format(sum_odd,sum_even))

#7.求1到5阶乘之和
sum2 = 0
n=1
for i in range(1, 6):
    n *= i
    sum2 += n
print(sum2)

#8.输入一个整数，判断他是否是素数。
n = int(input("plz input number"))
flag = True
edge = int(n**0.5)
for i in range(2,edge):
    if n % i == 0:
        flag = False
        break
print('prime number' if flag else 'not prime number')