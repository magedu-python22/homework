# -*- coding: utf-8 -*-
# @file   : ATM01.py
# @author : wfs
# @date   : 2019/06/11
# @version: 1.0
# @desc   : ATM模拟系统


"""
通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
(1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
(2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
(3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
(4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
(5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
ps:实现方式不限
"""

import os

ucount = 0
pcount = 0
money = 0

print("欢迎来到蓝翔银行，请输入序号选择对应的功能".center(50, "*"))
print("1:登陆验证\n" + "2:用户注册\n" + "3:退出系统")
choice = input("请输入你的选择：")
flag = "false"


# 用户注册功能

def register():
    global money
    global username
    username = input("请输入用户名：")
    with open("./userInfo.txt", "r") as f:
        my_dict = eval(f.readline())
        print(type(my_dict))
    if username in my_dict.keys():
        print("用户名已存在，请重新输入！")
    else:
        iphone = input("请输入电话号码：")
        password = input("请输入密码：")
        print("用户注册成功！赠送您5000元！")
        money = 5000
        my_dict[username] = [password, money, iphone]
        print(str(my_dict))
        with open("./userInfo.txt", "a") as f:
            f.write(str(my_dict))


# 用户登陆功能
def login():
    global ucount
    global pcount
    global flag
    global username
    global my_dict
    while True:
        username = input("请输入你的用户名：")
        with open("./userInfo.txt", "r") as f:
            my_dict = eval(f.readline())
        if username not in my_dict.keys():
            print("用户名不存在,请检查后再输入！")
            ucount += 1
            if ucount == 3:
                print("输入的用户名错误次数太多，退出系统！")
                break
        else:
            while True:
                password = input("请输入你的密码：")
                if my_dict[username][0] != password:
                    print("密码输入错误，请重新输入！")
                    pcount += 1
                    if pcount == 3:
                        print("输入的密码错误次数太多，退出系统！")
                        flag = "True"
                        break
                else:
                    print("登陆成功！")
                    print("1:菜单界面")
                    login_choice = input("请输入对应序号选择相应的功能：")
                    if login_choice == "1":
                        menu()
                    else:
                        print("输入错误，请输入密码后重新输入：")
                        break
        if flag == "True":
            break


# 菜单界面功能
def menu():
    global money
    print("欢迎进入蓝翔银行管理系统，请输入序号选择对应的功能".center(50, "*"))
    while True:
        print("1：查询余额\n" + "2：转账\n" + "3：取款\n" + "4：存款\n" + "5：退出当前菜单")
        options = input("请输入你的选择：")
        if options == "1":
            print("用户{}的余额为{}元。".format(username, my_dict[username][1]))
        elif options == "2":
            tranAmount = int(input("请输入你要转账的金额："))
            if my_dict[username][1] < tranAmount:
                print("金额不足，请重新输入！")
            else:
                money = my_dict[username][1] - tranAmount
                my_dict[username][1] = money
        elif options == "3":
            removeMoney = int(input("请输入你要取款的金额："))
            if my_dict[username][1] < removeMoney:
                print("金额不足，请重新输入！")
            else:
                money = my_dict[username][1] - removeMoney
                my_dict[username][1] = money
        elif options == "4":
            deposit = int(input("请输入你要存款的金额："))
            money = my_dict[username][1] + deposit
            my_dict[username][1] = money
        elif options == "5":
            break
        else:
            print("输入错误，退出系统！")
            os.system(exit(1))

if choice == "1":
    login()
elif choice == "2":
    register()
elif choice == "3":
    os.system(exit(0))
else:
    print("输入错误，退出系统！")
    os.system(exit(1))



