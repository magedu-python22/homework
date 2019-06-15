"""
通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
(1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
(2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
(3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
(4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
(5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
ps:实现方式不限
"""


def register(users):  # 注册
    new_user = input("输入用户名>>>").strip()
    while new_user in users:
        new_user = input("用户存在，输入用户名>>>").strip()
    new_password = input("请输入密码>>>").strip()
    phone = input("输入手机号码>>>").strip()
    users.update({new_user: {"password": new_password, "phone": phone, "balance": 5000}})
    print("注册成功")
    save_data(users)


def login(users):  # 登录
    user_count = 0
    pwd_count = 0
    login_user = input("请输入用户名>>>").strip()
    while login_user not in users:
        user_count += 1
        if user_count == 3:
            exit("输错3次，系统退出")
        login_user = input("用户不存在，请重新输入>>>").strip()
    login_pwd = input("输入密码>>>").strip()
    while login_pwd != users[login_user]["password"]:
        pwd_count += 1
        if pwd_count == 3:
            exit("输错密码3次，系统退出")
        login_pwd = input("密码不对，请重新输入>>>").strip()
    print("登录成功")
    return login_user


def check_balance(users, login_user):  # 查余额
    print("您的余额是{}".format(users[login_user]["balance"]))


def withdraw(users, login_user):  # 取款
    str = input("请输入您的取款金额>>>").strip()
    while not str.isdecimal():
        str = input("输入有误，请重新输入取款金额>>>").strip()
    withdraw_amount = int(str)
    while withdraw_amount > users[login_user]["balance"]:
        str = input("余额不足，请重新输入取款金额>>>").strip()
        while not str.isdecimal():
            str = input("输入有误，请重新输入正确金额>>>").strip()
        withdraw_amount = int(str)
    users[login_user]["balance"] -= withdraw_amount
    print("取款成功，您的余额为{}".format(users[login_user]["balance"]))
    save_data(users)


def deposit(users, login_user):  # 存款
    str = input("请输入您的存款金额>>>").strip()
    while not str.isdecimal():
        str = input("输入有误，请输入正确金额>>>").strip()
    deposit_amount = int(str)
    users[login_user]["balance"] += deposit_amount
    print("存款成功，当前余额为{}".format(users[login_user]["balance"]))
    save_data(users)


def transfer(users, login_user):  # 转账
    trans_user = input("请输入您要转账到的用户>>>").strip()
    while trans_user not in users:
        trans_user = input("输入的用户不存在，重新输入>>>").strip()
    str = input("请输入转账金额>>>").strip()
    while not str.isdecimal():
        str = input("输入有误，请输入正确金额>>>").strip()
    trans_amount = int(str)
    while trans_amount > users[login_user]["balance"]:
        str = input("输入金额大于您的余额，请重新输入>>>").strip()
        while not str.isdecimal():
            str = input("输入有误，请重新输入正确金额>>>").strip()
        trans_amount = int(str)
    users[login_user]["balance"] -= trans_amount
    users[trans_user]["balance"] += trans_amount
    print("转账成功")
    save_data(users)


def save_data(users):
    file = open('user.txt', 'w')
    file.write(str(users))
    file.close()


def read_data():
    file = open('user.txt', 'r')
    str = file.read()
    users = eval(str)
    file.close()
    return users


def menu():
    print("="*40)
    print(" "*10 + "银行ATM机模拟系统")
    print("  1.余额  2.存款  3.取款  4.转账  5.退出")
    print("="*40)


if __name__ == '__main__':
    print("-----欢迎使用ATM机模拟系统----")
    users = read_data()
    while True:
        login_choose = input("选择操作：1.登录 2.注册 3.退出>>>").strip()
        if login_choose == "1":
            login_user = login(users)
            while True:
                menu()
                choose = input("请输入您要执行的操作>>>").strip()
                if choose == "1":
                    check_balance(users, login_user)
                elif choose == "2":
                    deposit(users, login_user)
                elif choose == "3":
                    withdraw(users, login_user)
                elif choose == "4":
                    transfer(users, login_user)
                elif choose == "5":
                    break
                else:
                    choose = input("输入有误，重新输入>>>").strip()
        elif login_choose == "2":
            register(users)
        elif login_choose == "3":
            exit("退出系统")
        else:
            print("输入有误")