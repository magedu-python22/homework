#!/usr/bin/env python
# coding: utf-8

# In[8]:


d = dict((('zhangsan', 123),('lisi', 456),('wangmazi', 789)))
f = dict(passwd=0, balance=0, phone=0)
x = {}
scounter = 0
uc = 0
pc = 0

us = 0
flag = False

while True:
    for i in range(3):
        u = input('请输入您的账号>>>')
        if u not in d.keys():
            uc += 1
            if uc < 3:
                print('用户不存在，请重试')
            if uc == 3:
                print('您不是我行用户，3次登陆尝试已用完，请注册再来谢谢')
                break  
        if u in d.keys():
            us += 1
            print('用户名验证成功,您输入的用户名是:')
            print(u)
            d[u] = f
            x = d     
            d.update({'zhangsan':{'passwd':123, 'balance':100, 'phone':18012345678}})
            d.update({'lisi':{'passwd':456, 'balance':200, 'phone':18012345678}})
            d.update({'wangmazi':{'passwd':789, 'balance':300, 'phone':18012345678}})
#             print(x)
            
            with open('/home/python/projects/web/xdict.txt', 'w+', encoding='utf-8', errors='ignore') as f:
                f.write(str(x))
            with open('/home/python/projects/web/xdict.txt', 'r+', encoding='utf-8', errors='ignore') as f:
                print(f.read())
#             f = open('xdict.txt', 'w+', encoding='utf-8')
#             f.write(str(x))
#             f.close()
            
            for j in range(3):
                p = int(input('请输入您的密码>>>')) 
                if (u == 'zhangsan' and p == x['zhangsan']['passwd']) or (u == 'lisi' and p == x['lisi']['passwd']) or (u == 'wangmazi' and p == x['wangmazi']['passwd']):
                    print('登陆成功')
                    flag = True
                    scounter += 1
                    print('欢迎您使用，广东珠江银行网上银行')
                    print('0==> 余额查询')
                    print('1==> 用户转账')
                    print('2==> 用户注册')
                    print('3==> 返回主菜单')
                    num = int(input('请输入您所需要的服务>>>'))
                    if num == 0:
                        print('您的余额是：')
                        print(x[u]['balance'])
                    elif num == 1:
                        print('请输入您所需要转入的账号：')
                        u1 = input('>>>')
                        print('账号验证成功,您输入的账号是:')
                        print(u1)
                        print('请输入您所需要转入的金额：')
                        money = int(input('>>>'))
                        print('转入成功,您本次转账金额是:')
                        print(money)
                        tmp1 = x[u1]['balance'] + money
                        x.update({u1:{'balance':tmp1}}) 
                        print(x[u1]['balance'])
                        
                        tmp = x[u]['balance'] - money
                        x.update({u:{'balance':tmp}})
                        print('转入成功,您的余额为:')
                        print(x[u]['balance'])  
                        
                        with open('/home/python/projects/web/xdict.txt', 'w+', encoding='utf-8') as f:
                            f.write(str(x))
                        with open('/home/python/projects/web/xdict.txt', 'r+', encoding='utf-8', errors='ignore') as f:
                            print(f.read())            
#                         f = open('xdict.txt', 'w+', encoding='utf-8')
#                         f.write(str(x))
#                         f.close()
                    elif num == 2:
                        print('用户注册')
                        print('请输入您的账号：')
                        while True:
                            u2 = input('>>>')
                            if u2 in d.keys():
                                print(u2)
                                print('用户名已存在,请您重新输入:')
                            else:
                                print('账号验证成功,您即将注册的账号是:')
                                print(u2)
                                break
                                
                        p2 = int(input('请输入您的密码>>>'))
                        ph2 = int(input('请输入您的电话号码>>>'))
                        x.update({u2:{'passwd':p2, 'balance':5000, 'phone':ph2}})
                        print('您的注册信息账号,密码，电话依次为：')
                        print(u2,p2,ph2)
                        print(x)
                        
                        with open('/home/python/projects/web/xdict.txt', 'w+', encoding='utf-8') as f:
                            f.write(str(x))
                        with open('/home/python/projects/web/xdict.txt', 'r+', encoding='utf-8', errors='ignore') as f:
                            print(f.read())
#                         f = open('xdict.txt', 'w+', encoding='utf-8')
#                         f.write(str(x))
#                         f.close()
                    else:
                        if num == 3:
                            print('返回主菜单')
                            break

                else:
                    pc += 1
                    if pc < 3 and j < 2:
                        print('密码错误，请重新输入')

                    if pc == 3 and j == 2:
                        print('密码错误，登陆次数已用完，系统退出')
                        break


    if not flag:
        if scounter > 1 and us > 1:
            print('您已登陆成功')
            print('欢迎使用广东珠江银行网上银行系统')
            print('0==> 余额查询')
            print('1==> 用户转账')
            print('2==> 用户注册')
            print('3==> 返回主菜单')
            num = int(input('请输入您所需要的服务>>>'))
            if num == 0:
                print('余额查询')
            elif num == 1:
                print('用户转账')
            elif num == 2:
                print('用户注册')
            else:
                if num == 3:
                    print('返回主菜单')
                    break

"""
1. 运行 应该是主菜单吧
2. d.update({'zhangsan':{'passwd':123, 'balance':100, 'phone':18012345678}})
            d.update({'lisi':{'passwd':456, 'balance':200, 'phone':18012345678}})
            d.update({'wangmazi':{'passwd':789, 'balance':300, 'phone':18012345678}})
这些应该在运行之前就初始化好的吧？
3. 默认情况下：程序在运行期间，数据是保存在内存中的，退出的时候才会写入到文件里面
"""