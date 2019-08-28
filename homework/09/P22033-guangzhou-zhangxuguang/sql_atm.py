import pymysql


# 注册
def register():
    while True:
        new_user = input("输入用户名>>>").strip()
        with conn as cursor:
            with cursor:
                sql = "select * from users where userid = '{0}'".format(new_user)
                rows = cursor.execute(sql)
        if rows:
            print('用户已存在,', end='')
        else:
            break
    new_password = input("请输入密码>>>").strip()
    phone = input("输入手机号码>>>").strip()
    with conn as cursor:
        sql = "insert into users values('{0}','{1}','{2}',5000)".format(
            new_user, new_password, phone)
        cursor.execute(sql)
    print("注册成功")


# 登录
def login():
    user_count = 0
    pwd_count = 0

    while True:
        username = input("请输入用户名>>>").strip()
        with conn as cursor:
            with cursor:
                sql = "select * from users where userid = '{0}'".format(username)
                rows = cursor.execute(sql)
                login_user = cursor.fetchall()
        if not rows:
            user_count += 1
            if user_count == 3:
                exit("输错3次，系统退出")
            print('用户不存在,', end='')
        else:
            break
    login_pwd = input("输入密码>>>").strip()

    while login_pwd != login_user[0][1]:
        pwd_count += 1
        if pwd_count == 3:
            exit("输错密码3次，系统退出")
        login_pwd = input("密码不对，请重新输入>>>").strip()
    print("登录成功")
    return username


# 查余额
def check_balance(username):
    with conn as cursor:
        with cursor:
            sql = "select balance from users where userid = '{0}'".format(username)
            cursor.execute(sql)
            username = cursor.fetchone()[0]
    return username


# 取款
def withdraw(username):
    money = input("请输入您的取款金额>>>").strip()
    while not money.isdecimal():
        money = input("输入有误，请重新输入取款金额>>>").strip()
    withdraw_amount = int(money)
    while withdraw_amount > check_balance(username):
        money = input("余额不足，请重新输入取款金额>>>").strip()
        while not str.isdecimal():
            money = input("输入有误，请重新输入正确金额>>>").strip()
        withdraw_amount = int(money)
    balance = check_balance(username) - withdraw_amount
    with conn as cursor:
        with cursor:
            sql = "update users set balance = {0} where userid = '{1}'".format(
                balance, username)
            cursor.execute(sql)
            log_sql = "insert into log_moneys(userid, change_amount, ctype) values ('{0}','{1}',1)".format(
                username, -withdraw_amount)
            cursor.execute(log_sql)
    print("取款成功，您的余额为{}".format(balance))


# 存款
def deposit(username):
    money = input("请输入您的存款金额>>>").strip()
    while not money.isdecimal():
        money = input("输入有误，请输入正确金额>>>").strip()
    deposit_amount = int(money)
    balance = check_balance(username) + deposit_amount
    with conn as cursor:
        with cursor:
            sql = "update users set balance = {0} where userid = '{1}'".format(
                balance, username)
            cursor.execute(sql)
            log_sql = "insert into log_moneys(userid, change_amount, ctype) values ('{0}','{1}',2)".format(
                username, deposit_amount)
            cursor.execute(log_sql)
    print("存款成功，当前余额为{}".format(balance))


# 转账
def transfer(username):
    while True:
        trans_user = input("请输入您要转账到的用户>>>").strip()
        with conn as cursor:
            with cursor:
                sql = "select * from users where userid = '{0}'".format(trans_user)
                rows = cursor.execute(sql)
        if not rows:
            print('用户不存在,', end='')
        else:
            break
    money = input("请输入转账金额>>>").strip()
    while not money.isdecimal():
        money = input("输入有误，请输入正确金额>>>").strip()
    trans_amount = int(money)
    while trans_amount > check_balance(username):
        money = input("输入金额大于您的余额，请重新输入>>>").strip()
        while not str.isdecimal():
            money = input("输入有误，请重新输入正确金额>>>").strip()
        trans_amount = int(money)
    login_balance = check_balance(username) - trans_amount
    trans_balance = check_balance(trans_user) + trans_amount
    with conn as cursor:
        with cursor:
            login_sql = "update users set balance = {0} where userid = '{1}'".format(
                login_balance, username)
            cursor.execute(login_sql)
            log_sql = "insert into log_moneys(userid, change_amount, ctype, about) values ('{0}','{1}',3 ,'{2}')".format(
                username, -trans_amount, trans_user)
            cursor.execute(log_sql)
            trans_sql = "update users set balance = {0} where userid = '{1}'".format(
                trans_balance, trans_user)
            cursor.execute(trans_sql)
            log_sql = "insert into log_moneys(userid, change_amount, ctype, about) values ('{0}','{1}',3 ,'{2}')".format(
                trans_user, trans_amount, username)
            cursor.execute(log_sql)

    print("转账成功")


# 银行流水
def log_money(username):
    with conn as cursor:
        with cursor:
            sql = "select * from log_moneys where userid = '{0}'".format(username)
            rows = cursor.execute(sql)
            if not rows:  # 查询的数据为空时抛出NoExist的异常
                try:
                    raise Exception("NoExist")
                except Exception as e:
                    print(e)
            result = cursor.fetchall()
    for i in result:
        print(i)


# 菜单
def menu():
    print("="*48)
    print(" "*15 + "银行ATM机模拟系统")
    print("  1.余额  2.存款  3.取款  4.转账  5.流水  6.退出")
    print("="*48)
    print(end='')


if __name__ == '__main__':
    print("-----欢迎使用ATM机模拟系统----")
    print(end='')
    conn = pymysql.connect('127.0.0.1', 'guang', 'guang', 'atm')
    while True:
        login_choose = input("选择操作：1.登录 2.注册 3.退出>>>").strip()
        if login_choose == "1":
            login_user = login()
            while True:
                menu()
                print(end='')
                choose = input("请输入您要执行的操作>>>").strip()
                if choose == "1":
                    print("您的余额是'{}'元".format(check_balance(login_user)))
                elif choose == "2":
                    deposit(login_user)
                elif choose == "3":
                    withdraw(login_user)
                elif choose == "4":
                    transfer(login_user)
                elif choose == "5":
                    log_money(login_user)
                elif choose == "6":
                    break
                else:
                    choose = input("输入有误，重新输入>>>").strip()
        elif login_choose == "2":
            register()
        elif login_choose == "3":
            conn.close()
            exit("退出系统")
        else:
            print("输入有误")