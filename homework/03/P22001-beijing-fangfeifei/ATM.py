# -*- coding:utf-8 -*-
# @Time    : 2019/8/6 16:10
# @Author  : FANG FEIFEI 
# @FileName: ATM.py
# @Software: PyCharm
'''
通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
(1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
(2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
(3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
(4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
(5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
ps:实现方式不限
'''

def mainPage():
    print('ATM'.center(20, '*'))
    print('1.登录')
    print('2.注册')
    print('0.退出')
    print('*'*20)
    print('请输入菜单：', end='')
    selectNum = int(input())
    if selectNum == 1:
        loginPage()
    elif selectNum == 2:
        register()
    else:
        quit()


def userMainPage(id,userInfo):
    print((id + '-用户中心').center(20, '*'))
    print('1.余额')
    print('2.转账')
    print('3.取款')
    print('4.存款')
    print('5.主页')
    print('0.退出')
    print('*' * 20)
    print('请输入菜单：',end='')
    selectNum = int(input())
    if selectNum == 1:
        queryBalance(id)
    elif selectNum == 2:
        transferAccounts(id, userInfo)
    elif selectNum == 3:
        withdrawal(id, userInfo)
    elif selectNum == 4:
        deposit(id, userInfo)
    elif selectNum == 5:
        mainPage()
    else:
        quit()

def loginPage():
    id = input("请输入账号：")
    password = input("请输入密码：")
    userInfo,isSucceed,msg = userLogin(id, password)
    if isSucceed==False:
        print(msg)
        mainPage()
    else:
        userMainPage(id, userInfo)


def userLogin(id,password):
    isSucceed = True
    msg = ''
    user = ''
    userInfo = {}
    userDict = getUserDict()
    if id not in userDict.keys():
        isSucceed  =  False
        msg = '提示：账号错误！'
    elif userDict[id]['password'] != password:
        isSucceed = False
        msg = '提示：密码错误！'
    else:
        userInfo = userDict[id]
    return userInfo,isSucceed,msg

def register():
    print('新用户注册'.center(20, '*'))
    id = input("请输入账号：")
    password = input("请输入密码：")
    phone = input("请输入手机号：")
    balance = 5000

    userDict = getUserDict()
    if id in userDict.keys():
        print('账号“{0}”已存在，请重新注册!'.format(id))
    else:
        userDict[id] = {'password': password, 'phone': phone, 'balance': balance}
        saveUserDict(userDict)
        print('账号“{0}”已注册成功，新用户免费赠送 {1} 元，请查收!'.format(id, balance))
    mainPage()

def getUserDict():
    userdict = {}
    with open("UserInfo.txt", "r") as f:
        userdict = eval(f.readline())
    return userdict

def saveUserDict(userDict):
    file = open("UserInfo.txt", 'w')
    file.write(str(userDict))
    file.close()

def getUserInfo(id):
    userDict = getUserDict()
    isSucceed = False
    userInfo = {}
    if id in userDict.keys():
        isSucceed = True
        userInfo = userDict[id]
        msg = '提示：账号正确！'
    else:
        msg = '提示：账号错误！'
    return userInfo, isSucceed, msg

#查余额
def queryBalance(id):
    userInfo, isSucceed, msg = getUserInfo(id)
    print('您的账号余额为：{0} 元'.format(userInfo['balance']))
    userMainPage(id, userInfo)

#转账
def transferAccounts(id, userInfo):
    isOk = False
    isGo = True
    tid = ''
    money = ''
    while isGo:
        tid = input("请输入收款人账号：")
        tuserInfo, isSucceed, msg = getUserInfo(tid)
        if isSucceed == False:
            print(msg)
            continue
        password = input("请输入账号密码：")
        if userInfo['password'] == password:
            money = int(input("请输入转账金额："))
            if userInfo['balance'] < money:
                print('您的余额已不足！')
                continue
            else:
                isOk = True
                isGo = False
        else:
            print('密码输入错误！')

    if isOk == True:
        userDict = getUserDict()
        userDict[id] = {'password': userInfo['password'], 'phone': userInfo['phone'],'balance': userInfo['balance'] - money}
        userDict[tid] = {'password': tuserInfo['password'], 'phone': tuserInfo['phone'],'balance': tuserInfo['balance'] + money}
        saveUserDict(userDict)
        print('转账成功!您的账户余额：{0} 元'.format(userInfo['balance'] - money))
    userMainPage(id, userInfo)

#取款
def withdrawal(id, userInfo):
    password = input("请输入账号密码：")
    if userInfo['password'] == password:
        money = int(input("请输入取款金额："))
        if userInfo['balance'] < money:
            print('您的余额已不足！')
        else:
            userDict = getUserDict()
            userDict[id] = {'password': userInfo['password'], 'phone': userInfo['phone'], 'balance': userInfo['balance'] - money}
            saveUserDict(userDict)
            print('取款成功!您的账户余额：{0} 元'.format(userInfo['balance'] - money))

    userMainPage(id, userInfo)

def deposit(id, userInfo):
    money = int(input("请输入存款金额："))
    userDict = getUserDict()
    userDict[id] = {'password': userInfo['password'], 'phone': userInfo['phone'], 'balance': userInfo['balance'] + money}
    saveUserDict(userDict)
    print('存款成功!您的账户余额：{0} 元'.format(userInfo['balance'] + money))
    userMainPage(id, userInfo)

if __name__ == '__main__':
    mainPage()

    """
    逻辑很清晰，写的很好
    """