#!/usr/bin/env python
# _*_ coding: utf-8 _*_

#########################################################################
#  Created Time: 2019-06-11 23:38:43 2 下午
#  File Name: test.py
#########################################################################

import getpass
import json
import sys

# 登陆
user = str(input('请输入用户名：').strip())
passwd = str(getpass.getpass('请输入密码：').strip())
message="""请输入编号以启用功能：
    1、查看余额
    2、转账汇款
    3、退出
"""

fpath='data.json'

# 读取json
with open(fpath, 'r') as f:
    data = json.load(f)
    f.close


# 功能
flag = False
try:
    data[user]
except KeyError:
    print('用户不存在,请先创建用户：')
    # 用户信息，user，passwd其实可以使用上面已输入的
#     user = str(input('请输入用户名：').strip())
#     passwd = str(getpass.getpass('请输入密码：').strip())
    for i in range(4):
        if i == 3:
            print('超出最大重试次数，退出！')
            sys.exit(1)
        passwd1 = str(getpass.getpass('请再次输入密码：').strip())
        if passwd == passwd1:
            break
    email = str(input('请输入电子邮件地址：').strip())
    phone = int(input('请输入手机号码：').strip())
    d1 = {'passwd': passwd, 'email': email, 'phone': phone, 'money': 5000}
    data[user] = d1
    with open(fpath, 'w') as f:
        json.dump(data, f)
        f.close()
    flag = True
else:
    flag = True

for i in range(3):
    if flag:
        if  data[user]['passwd'] == passwd:
            for z in range(4):             # 设置可选编号最大次数为3次
                if z == 3:
                    print('超出最大重试次数！')
                    break
                n = int(input(message).strip())

                # 查询余额
                if n == 1:
                    print('余额：' + str(data[user]['money']))
                    break

                # 转账汇款
                elif n == 2:
                    flag = False
                    user1 = str(input('请输入收款人：').strip())
                    for x in range(4):
                        try:
                            data[user1]
                        except KeyError:
                            if x == 2:
                                print('超出最大重试次数！')
                                break
                            print('收款人用户名未找到或不存在！\n')
                            user1 = str(input('请重新输入收款人：').strip())
                        else:
                            flag = True
                            break

                    if flag:
                        for y in range(4):
                            money1 = int(input('请输入转账金额：').strip())
                            if money1 <= data[user]['money']:
                                data[user]['money'] = (data[user]['money'] - money1)
                                data[user1]['money'] = (data[user1]['money'] + money1)
                                print(f"已向{user1}转账{money1}，您的余额为：{data[user]['money']}")
                                with open(fpath, 'w') as f:
                                    json.dump(data, f)
                                    f.close()
                                break
                            else:
                                if y == 3:
                                    print('超出最大重试次数！')
                                    break
                                print("金额不足，请重新输入！")
                                print(f"您的余额为：{data[user]['money']}")
                    break

                # 退出
                elif n == 3:
                    break
                else:
                    print('编号输入错误，请重新输入\n')
            if flag:
                break

        else:
            if i == 2:
                print('超出最大重试次数！')
            else:
                passwd = str(getpass.getpass('密码错误，请重新输入密码：').strip())
