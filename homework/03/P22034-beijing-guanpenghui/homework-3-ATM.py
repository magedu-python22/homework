# 用户注册
def register():
    username = input('请输入用户名:')
    if username not in userinfo.keys():
        if username == '':
            print('用户名不能为空，请重新输入')
            register()
        else:
            passwd = input('请输入密码:')
            if passwd == '':
                print('密码不能为空，请重新输入')
                register()
            userlogininfo[username] = passwd
            userinfo.setdefault(username, 5000)
    else:
        print('您输入的用户名在系统中已存在，请重新输入')
        register()
    return username


# 用户登录
def login():
    unamecount = 3
    upasswdcount = 3
    while unamecount and upasswdcount:
        loginname = input('请输入用户名：')
        password = input('请输入密码:')
        if loginname in userlogininfo.keys() and password == userlogininfo[loginname]:
            return loginname
        elif loginname not in userlogininfo.keys():
            unamecount -= 1
            print('用户名剩余错误次数', unamecount)
            if unamecount == 0:
                print('用户名错误超过三次，系统将退出')
                return 99
                break
            else:
                print('用户名错误，还有{}次机会，请重新输入'.format(unamecount))
                continue
        else:
            upasswdcount -= 1
            print('密码错误剩余次数', upasswdcount)
            if upasswdcount == 0:
                print('密码错误超过三次，系统将退出')
                return 99
                break
            else:
                print('密码错误，还有{}次机会，请重新输入'.format(upasswdcount))
                continue


# 定义注册登录界面
def graphInterface():
    print('''======欢迎使用小明银行======
用户注册 请按1
用户登录 请按2
============================''')
    number = input('请选择:')
    return number


# 定义功能界面
def func():
    print('''======欢迎使用小明银行======
余额查询   请按1
转    账   请按2
存    款   请按3
取    款   请按4
退    出   请按5
============================''')
    funcnum = int(input('请选择:'))
    return funcnum


# 返回功能模块
def goback():
    print('''======欢迎使用小明银行======
退      出   请按1
返回上一层   请按2
============================''')
    gobacknumber = int(input('请选择:'))
    return gobacknumber


# 退出
def ex():
    print('谢谢您的使用,再见')


# 功能选择
def funcselect(fnumber):
    if fnumber == 1:
        print('您好{},您的账户可用余额为{}元'.format(checkname, userinfo[checkname]))
        gnumber = goback()
        return gnumber
    elif fnumber == 2:
        destname = input('请输入要转账的用户名：')
        if destname not in userinfo.keys():
            print('您好{},转账未完成,{}用户不存在,请您再次确认用户名是否正确'.format(checkname, destname))
            gnumber = goback()
            return gnumber
        elif destname == checkname:
            print('您好{},您不能给自己转账,请您输入其他用户'.format(destname))
            gnumber = goback()
            return gnumber
        else:  # destname in userinfo.keys() and destname != checkname:
            depo = int(input('请输入转账金额：'))
            if depo > userinfo[checkname]:
                print('您的转账金额超出账户余额，请重新输入')
            else:
                userinfo[checkname] -= depo
                userinfo[destname] += depo
                print('您好{},转账已完成,您的账户剩余金额为{}'.format(checkname, userinfo[checkname]))
            gnumber = goback()
            return gnumber
    elif fnumber == 3:
        depo = int(input('请输入您要存款的金额:'))
        userinfo[checkname] += depo
        print('您好{},存款成功，您的账户剩余金额为{}'.format(checkname, userinfo[checkname]))
        gnumber = goback()
        return gnumber
    elif fnumber == 4:
        depo = int(input('请输入您要取款的金额:'))
        if depo > userinfo[checkname]:
            print('您的取款金额超出账户余额，请重新输入')
        else:
            userinfo[checkname] -= depo
            print('您好{},请在取款口取款，您的账户剩余金额为{}'.format(checkname, userinfo[checkname]))
        gnumber = goback()
        return gnumber
    else:
        pass

# 主程序
userlogininfo = {'zhangsan': '123456', 'lisi': '123456'}
userinfo = {'zhangsan': 5000, 'lisi': 5000}
num = graphInterface()
if num == '1':
    checkname = register()
    print('您好:{},帐号注册成功，您的账户剩余金额为{}'.format(checkname, userinfo[checkname]))
    while True:
        fnumber = func()
        gnumber = funcselect(fnumber)
        if gnumber == 2:
            continue
        else:
            ex()
            break
elif num == '2':
    checkname = login()
    if checkname == 99:
        ex()
    else:
        print('您好:{},帐号登录成功，您的账户剩余金额为{}'.format(checkname, userinfo[checkname]))
        while True:
            fnumber = func()
            gnumber = funcselect(fnumber)
            if gnumber == 2:
                continue
            else:
                ex()
                break
else:
    print('输入错误，请重新输入')