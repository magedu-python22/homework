#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/11 10:41
# 通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
# (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
# (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
# (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
# (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
import json
filename = 'userdicfile.json'
with open(filename) as f:
    userdic = json.load(f)


# 写入文件
def writeuserdic():
    with open(filename, 'w+') as f:
        json.dump(userdic, f)


# 用户注册
def signup():
    while True:
        uid = input('请输入用户名：(输入空则退出)')
        if uid == '' or uid.isspace():
            return ATM()
        if userdic.get(uid, 0):
            print('用户名已存在，请重新输入')
            continue
        else:
            pwd = input('请输入密码：')
            tel = input('请输入电话号码：')
            m = 5000
            userdic[uid] = [pwd, tel, m]
            writeuserdic()

# 登陆验证
def signin():
    while True:
        uid = input('请输入用户名：(输入空则退出)')
        if uid == '' or uid.isspace():
            return ATM()
        if userdic.get(uid, 0):
            for i in range(1, 4):
                pwd = input('请输入密码：')
                if pwd == userdic[uid][0]:
                    return lst(uid)
                else:
                    print('密码错误第{}次'.format(i))
            else:
                print('密码错误超过三次系统退出')
                return None
        else:
            print('该用户不存在')


# 菜单界面
def lst(uid):
    command = dict(zip(range(1, 6), (useradm(uid), pwdalter(uid), infoalter(uid), ATM(), None)))
    print('''
    1.账户管理
    2.修改密码
    3.修改电话号码
    4.返回上一级
    5.退出
    ''')
    choice2 = int(input('请输入对应的序列号以执行命令'))
    if command[choice2]:
        return command[choice2]
    else:
        return None


# 查看账户余额
def currentm(uid):
    print('当前余额为：', userdic[uid][2])


# 账户管理(查看自己账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能)
def useradm(uid):
    while True:
        print('''
        1.查看当前余额
        2.转账
        3.存款
        4.取款
        5.返回上一级
        6.退出
        ''')
        choice3 = int(input('请输入对应的序列号以执行命令'))
        if choice3 == 1:
            currentm(uid)
        elif choice3 == 2:
            uid1 = input('请输入其他账户用户名：')
            m = int(input('请输入转账金额：'))
            if userdic.get(uid1, 0):
                userdic[uid][2] = userdic[uid][2] - m
                userdic[uid1][2] = userdic[uid1][2] + m
                currentm(uid)
            else:
                print('该用户不存在')
        elif choice3 == 3:
            currentm(uid)
            m = int(input('请输入存款金额：'))
            userdic[uid][2] = userdic[uid][2] + m
            currentm(uid)
        elif choice3 == 4:
            currentm(uid)
            m = int(input('请输入取款金额：'))
            userdic[uid][2] = userdic[uid][2] - m
            currentm(uid)
        elif choice3 == 5:
            return lst(uid)
        else:
            break
        writeuserdic()


# 修改密码
def pwdalter(uid):
    count = 1
    while count <= 3:
        pwd = input('请输入原密码：(输入空则退出)')
        if pwd == '' or pwd.isspace():
            return lst(uid)
        elif pwd == userdic[uid][0]:
            pwd = input('请输入新密码：')
            userdic[uid][0] = pwd
            writeuserdic()
        else:
            print('密码错误第{}次'.format(count))
            count += 1
    print('密码错误超过三次系统退出')
    return None


# 修改信息
def infoalter(uid):
    print(uid, userdic[uid][1])
    tel = input('请输入手机号码：(输入空则退出)')
    if tel == '' or tel.isspace():
        return lst(uid)
    userdic[uid][1] = tel
    writeuserdic()
    print(uid, userdic[uid][1])
    return lst(uid)


def ATM():
    command = dict(zip(range(1, 4), (signup(), signin(), None)))
    print('''
    1.用户注册
    2.用户登陆
    3.退出
    ''')
    choice1 = int(input('请输入对应的序列号以执行命令'))
    return command[choice1]


ATM()
