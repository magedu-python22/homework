'''
通过Python编程完成一个银行ATM机模拟系统，具备如下功能:
(1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
(2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
(3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
(4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
(5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
ps:实现方式不限
'''
#userinfo={"jaxzhai":{"password":"123","iphone":"18810099999","money":5000}}
import json
k = 0
status = 0
#with open("data","w") as f:
#    userinfo=json.dumps(f)
with open("data","r") as f:
    userinfo=json.load(f)
while True:
    print(u'''======欢迎使用花旗银行ATM存取款系统==，
                        1:用户注册 
                        2:用户登陆
          ==========请输入您的选择：==========''')
    choselogin = input(">>>>>")
    if choselogin == "1":
        username = input("请输入用户名")
        if username in userinfo:
            print("你输入的用户以存在")
            continue
        password = input("请输入密码")
        iphone = input("请输入手机号")
        userinfo[username]={"password":password,"iphone":iphone,"money":5000}
        with open("data", "w") as f:
            json.dump(userinfo,f)

    else:
        putuser = input("请输入用户名>>")
        putpasswd = input("请输入密码>>")
        if k >= 2:
            print("输入的次数超限")
            break
        else:
            if putuser in userinfo and userinfo[putuser]["password"] == putpasswd:
                print("登录成功")
                status = 1
                break
            elif putuser not in  userinfo:
                print("您输入的用户名不存在")
                k+=1
            else:
                print("您输入的密码不正确")
                k+=1

if status:
    while True:
        print(u'''======欢迎使用花旗银行ATM存取款系统=======================
        ====请输入你的选项，1:余额查询 2:存款 3:取款 4:转账 5:退出===
        =======================================================''')
        chose = input(">>>>:")
        if chose == "1":
            print("您的余额为：" , userinfo[putuser]["money"])
        elif chose == "2":
            print("存款")
            moneycun = int(input("请输入存款金额>>>:"))
            userinfo[putuser]["money"] += moneycun
            with open("data", "w") as f:
                json.dump(userinfo, f)
        elif chose == "3":
            print("取款")
            moneyqu = int(input("请输入取款金额>>>:"))
            if moneyqu > userinfo[putuser]["money"]:
                print("您取款金额超限")
            else:
                userinfo[putuser]["money"] -= moneyqu
                with open("data", "w") as f:
                    json.dump(userinfo, f)
        elif chose == "4":
            print("转账")
            userzhuan = input("请输入账号>>>:")
            if userzhuan in userinfo:
                moneyzhuan = int(input("请输入转账金额>>>:"))
                if moneyzhuan > userinfo[putuser]["money"]:
                    print("您转账金额超限")
                else:
                    userinfo[userzhuan]["money"] += moneyzhuan
                    userinfo[putuser]["money"] -= moneyzhuan
                    with open("data", "w") as f:
                        json.dump(userinfo, f)
            else:
                print("您输入的账户不存在")
        elif chose == "5":
            exit("sorry")
