#-*- comding:utf-8   -*-

# 通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
# (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
# (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
# (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
# (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
# ps:实现方式不限
import os

def read():
    with open('./week_3_atm.txt', "r") as f:
        info_dict = eval(f.readline())
        return info_dict

def write(info_dict):
    with open('./week_3_atm.txt', "w") as f:
        f.write(str(info_dict))

def register():#用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
    info_dict = read()
    count_register_error = 3  # 注册错误次数限制
    while count_register_error:
        username = input("请输入用户名：")
        if username in info_dict.keys():
            print("用户已存在，请重新输入！")
            count_register_error -= 1
        else:
            phone = input("请输入电话号码：")
            password = input("请输入密码:")
            money = 5000
            info_dict[username] = [password, money, phone]
            write(info_dict)
            print("用户注册成功，赠送您5000元")
            print('重新进入菜单')
            system()
    print('输入错误次数太多，请重新进入系统')

def login():#用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
    info_dict = read()
    count_login_error = 3  # 登录错误次数显示
    while count_login_error:
        username = input("请输入用户名：")
        password = input("请输入密码:")
        if username  in info_dict.keys() :
            print('登录成功')
            menu(username)
        else:
            print("用户或密码错误，请重新输入！")
            count_login_error -= 1
    print('输入错误次数太多，请重新进入系统')

def menu(username):
    # #登陆成功后显示功能操作界面，输入序号选择对应功能。用户名和密码以及账户信息等必须永久保存
    # #用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
    print('欢迎进入atm银行管理系统，请输入序号对应的功能')
    while True:
        print("1:查询余额\n" + "2:转账\n" + "3:取款\n" + "4:存款\n" + "5:退出当前菜单")
        choice = input("请输入您的选择:")
        if choice in ['1','2','3','4','5']:
            info_dict = read()
            if choice == "1":
                print("用户{0}的余额为{1}元.".format(username, info_dict[username][1]))
            elif choice == "2":
                transferAmount = int(input("请输入您要转账的金额:"))
                if info_dict[username][1] < transferAmount:
                    print("金额不足，请重新输入")
                else:
                    money = info_dict[username][1] - transferAmount
                    info_dict[username][1] = money
                    write(info_dict)
                    print("转账成功，您的余额为{}".format(info_dict[username][1]))
            elif choice == "3":
                withdrawalAmount = int(input("请输入您要取款的金额:"))
                if info_dict[username][1] < withdrawalAmount:
                    print("余额不足，请重新输入！")
                else:
                    money = info_dict[username][1] - withdrawalAmount
                    info_dict[username][1] = money
                    write(info_dict)
                    print("取款成功，您的余额为{}".format(info_dict[username][1]))
            elif choice == "4":
                depositAmount = int(input("请输入您要存款的金额:"))
                money = info_dict[username][1] + depositAmount
                info_dict[username][1] = money
                write(info_dict)
                print("存款成功，您的余额为{}".format(info_dict[username][1]))

            elif choice == "5":
                exit()

        else:
            print('没有这个功能，请重新选择')

def system ():
    while True:
        print('欢迎进入atm银行管理系统，请输入序号对应的功能'.center(50, "*"))
        print(" 1:登录\n", "2:用户注册\n", "3:退出系统")
        main_choice = input("请输入您的选择:")
        flag = "false"
        if main_choice == "1":
            login()
        elif main_choice == "2":
            register()
        elif main_choice == "3":
            os.system(exit(0))
        else:
            print("输入错误，重新选择".center(50, "*"))

if __name__ == '__main__':
    system()

