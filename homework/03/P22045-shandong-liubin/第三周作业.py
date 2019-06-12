from collections import defaultdict
usernamelist = []
usernamedict = defaultdict(lambda: [])
lst = ['用户登入', '用户注册', '退    出']
lst2 = ['查询余额', '转账功能', '存    款', '取    款', '返    回', '退    出']
def enter():# 登入
    print('欢迎进入XX银行网上银行，请输入以下编码进行操作')
    print("----编码-------名称--------")
    for key, value in enumerate(lst):
        print("----", key, "-----", value, "-----")
    print("---------------------------------")
    choice = input("请输入")
    if choice == "0":
        return landing()
    if choice == "1":
        return create()
    elif choice == "2":
        return print('3Q')
def landing():# 用户登陆
    while True:
        username = str(input("请输入你的账户"))
        if username=="0":
            return enter()
        elif username not in usernamelist:
            print('该用户不存在，请重新输入。返回请输入“0”')
            continue
        else:
            x=usernamedict[username]
            for i in range(3):
                password = str(input("请输入你的密码"))
                #print(x[0],password)
                d = 2 - i
                if password == x[0]:
                    return _landing(username)
                else:
                    print('密码错误，剩余输入次数：',d)
                    if d == 0:
                        print('密码错误次数过多，已退出')
                        break
    return enter()

def create():   # 创建用户
    while True:
        username = str(input("请输出你的账户"))
        if username == "0":
            break
        elif username in usernamelist:
            print("该用户已存在，请重新输入。输入“0”退出")
            continue
        else:
            password = str(input("请输入你的密码"))
            usernamedict[username].append(password)
            usernamedict[username].append(5000)
            usernamelist.append(username)
            print('创建成功！您的账户为:{}，密码为:{}。账户余额￥5000元'.format(username, password))
            break
    return enter()



def _landing(username):  #登录2
    def query(username):  # 账户查询
        print("您的余额为：￥", usernamedict[username][1], '。')
        print("返回上一层菜单请输入“0”")
        while True:
            ret=input("请输入")
            if ret == "0":
                return _landing(username)
            else:
                print("输入有误，请重新输入")
                continue

    def transfer(username):  # 转账
        username1 = str(input("请输入对方的账户"))
        if username1 not in usernamelist:
            print('该用户不存在，请重新输入。')
        else:
            while True:
                money = int(input("请输入转账金额"))
                # print(money,usernamedict[username][1])
                if money <= usernamedict[username][1]:
                    usernamedict[username1][1] += money
                    usernamedict[username][1] -= money
                    print('转账成功',"您的余额为：￥", usernamedict[username][1], '。')
                    # print (usernamedict)
                    break
                else:
                    print('您的余额不足，请重新输入')
                    continue
        print("返回上一层菜单请输入“0”")
        while True:
            ret = input("请输入")
            if ret == "0":
                return _landing(username)
            else:
                print("输入有误，请重新输入")
                continue
    def deposit(username):  # 存款
        money = int(input("请输入存入金额"))
        usernamedict[username][1] += money
        print('存入成功，您的余额为:￥{}元。'.format(usernamedict[username][1]))
        print("返回上一层菜单请输入“0”")
        while True:
            ret = input("请输入")
            if ret == "0":
                return _landing(username)
            else:
                print("输入有误，请重新输入")
                continue
    def out(username):  # 取款
        while True:
            money = int(input("请输入取出金额"))
            if money <= usernamedict[username][1]:
                usernamedict[username][1] -= money
                print('取出成功',"您的余额为：￥", usernamedict[username][1], '。')
                # print(usernamedict)
                break
            else:
                print('您的余额不足，请重新输入')
                continue
        print("返回上一层菜单请输入“0”")
        while True:
            ret = input("请输入")
            if ret == "0":
                return _landing(username)
            else:
                print("输入有误，请重新输入")
                continue
    print('欢迎进入XX银行网上银行，请输入以下编码进行操作')
    print("----编码-------名称--------")
    for key, value in enumerate(lst2):
        print("----", key, "-----", value, "-----")
    print("---------------------------------")
    choice = input("请输入")
    if choice == "0":
        return query(username)
    if choice == "1":
        return transfer(username)
    if choice == "2":
        return deposit(username)
    if choice == "3":
        return out(username)
    if choice == "4":
        return enter()
    elif choice == "5":
        return print('3Q')



enter()

