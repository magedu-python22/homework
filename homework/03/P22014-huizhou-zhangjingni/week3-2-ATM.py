#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:Miki
# Date : 2019/6/11 12:51
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

while True:
    print('''
    1.登陆
    2.注册
    3.退出
    ''')
    command = int(input('请输入序列号执行对应命令：'))
    # 登陆验证
    if command == 1:
        count = 0
        uid = input('请输入用户名：(输入空则退出)：')
        if uid == '' or uid.isspace():
            break
        while count <= 3:  # 密码错误超过三次系统退出
            if userdic.get(uid, 0):
                pwd = input('请输入密码：')
                if userdic[uid][0] == pwd:  # 密码正确进入 菜单界面
                    while True:
                        print('''
                        1.账户管理
                        2.修改密码
                        3.修改电话号码
                        4.返回上一级
                        5.退出
                        ''')
                        command1 = int(input('请输入序列号执行对应命令：'))
                        if command1 == 1: # 1.账户管理
                            while True:
                                print('''
                                1.查看当前余额
                                2.转账
                                3.存款
                                4.取款
                                5.返回上一级
                                6.退出
                                ''')
                                command2 = int(input('请输入序列号执行对应命令：'))
                                userm = userdic[uid][2]
                                if command2 == 1:  # 1.查看当前余额
                                    print(userm)
                                elif command2 == 2:  # 2.转账
                                    print('当前余额:', userm)
                                    uid1 = input('请输入其他账户用户名')
                                    m = int(input('请输入转账金额'))
                                    if userdic.get(uid1, 0):
                                        userm = userm - m
                                        userdic[uid1][2] = userdic[uid1][2] + m
                                        print('当前余额:', userm)
                                    else:
                                        print('该用户不存在')
                                elif command2 == 3:  # 3.存款
                                    print('当前余额:', userm)
                                    m = int(input('请输入存款金额'))
                                    userm = userm + m
                                    print('当前余额:', userm)
                                elif command2 == 4:  # 4.取款
                                    print('当前余额:', userm)
                                    m = int(input('请输入取款金额'))
                                    userm = userm - m
                                    print('当前余额:', userm)
                                elif command2 == 5:  # 5.返回上一级
                                    with open(filename, 'w+') as f:
                                        json.dump(userdic, f)
                                    break
                                else: # 6.退出
                                    with open(filename, 'w+') as f:
                                        json.dump(userdic, f)
                                    quit()
                        elif command1 == 2:  # 2.修改密码
                            pwd = input('请输入原密码：(输入空则退回上一级)')
                            if pwd == '' or pwd.isspace():
                                break
                            elif pwd == userdic[uid][0]:
                                pwd = input('请输入新密码：')
                                userdic[uid][0] = pwd
                                print('修改成功')
                                continue
                        elif command1 == 3:  # 3.修改电话号码
                            print(uid, userdic[uid][1])
                            tel = input('请输入手机号码：(输入空则退回上一级)')
                            if tel == '' or tel.isspace():
                                break
                            userdic[uid][1] = tel
                            print('修改成功')
                            print(uid, userdic[uid][1])
                            continue
                        elif command1 == 4:  # 4.返回上一级
                            with open(filename, 'w+') as f:
                                json.dump(userdic, f)
                            break
                        else: # 5.退出
                            with open(filename, 'w+') as f:
                                json.dump(userdic, f)
                            quit()
                else:
                    count += 1
                    print('密码错误第{}次'.format(count))
            else:
                print('该用户不存在')
            break
        else:
            print('密码错误超过三次系统退出')
            quit()

    # 用户注册
    elif command == 2:
        while True:
            uid = input('请输入用户名：(输入空则退回上一级)')
            if uid == '' or uid.isspace():
                break
            if userdic.get(uid, 0):
                print('用户名已存在，请重新输入')
            else:
                pwd = input('请输入密码：')
                tel = input('请输入电话号码：')
                m = 5000
                userdic[uid] = [pwd, tel, m]
                with open(filename, 'w+') as f:
                    json.dump(userdic, f)
    else:
        with open(filename, 'w+') as f:
            json.dump(userdic, f)
        break
