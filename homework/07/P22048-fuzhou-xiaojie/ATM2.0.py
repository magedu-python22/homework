import pickle


def login_first(name):
    print('---------------------------------------------')
    print('----0-----------------------------查询余额----')
    print('----1-----------------------------存    钱----')
    print('----2-----------------------------取    钱----')
    print('----3-----------------------------转    账----')
    print('----4-----------------------------修改密码----')
    print('----5-----------------------------注    销----')
    print('----6-----------------------------退    出----')
    print('---------------------------------------------')
    number1 = int(input('请根据提示输入数字: '))
    if number1 == 0:  # 查询余额
        print('当前余额为{}!'.format(database[name]['money']))
        return login_first(name)
    if number1 == 1:  # 存钱
        n = int(input('请输入要存入的金额: '))
        database[name]['money'] = (database[name]['money'] + n)
        database.update(database)
        print('存入成功!')
        print('当前账户余额为{}!'.format(database[name]['money']))
        return login_first(name)
    if number1 == 2:  # 取钱
        n = int(input('请输入要取出的金额: '))
        if n > database[name]['money']:
            print('余额不足!')
            print('取出失败!')

        else:
            database[name]['money'] = (database[name]['money'] - n)
            print('取出成功!')
            print('当前账户余额为{}!'.format(database[name]['money']))
        return login_first(name)
    if number1 == 3:
        name1 = input('请输入要转入的账户： ')
        if name1 in database:
            m = int(input('请输入要转入的金额： '))
            if m > database[name]['money']:
                print('余额不足，转入失败！')
            else:
                database[name]['money'] = (database[name]['money'] - m)
                database[name1]['money'] = (database[name1]['money'] + m)
                database.update(database)
                print('转账成功，当前用户余额为 {}'.format(database[name]['money']))
        else:
            print('用户不存在')
        return login_first(name)
    if number1 == 4:  # 修改密码
        p = {name: None}
        p[name] = input('请输入新密码: ')
        password.update(p)
        print('密码修改成功')
        return main()
    if number1 == 5:  #注销用户
        database.pop(name)
        return main()
    if number1 == 6:  # 返回上级菜单
        return main()
    else:  # 输入错误提示
        print('请根据提示输入!')
        return login_first(name)

def registered():    #  注册用户
    name = input('请输入用户名： ')
    if name not in database:
        d = {name: {'user name': None, 'phone': None, 'money': None}}
        p = {name: None}
        d[name]['user name'] = name
        p[name] = input('请输入密码: ')
        d[name]['phone'] = input('请输入手机号码: ')
        d[name]['money'] = 5000
        print('注册成功，赠送5000元，当前账户信息为：{}'.format(d.values()))
        return password.update(p), database.update(d)
    else:
        print('用户已存在!')

def main():
    global flag
    print('欢迎使用爱存不存ATM虚拟系统')
    print('---------------------------------------------')
    print('----0-----------------------------注    册----')
    print('----1-----------------------------登    录----')
    print('----2-----------------------------退    出----')
    print('---------------------------------------------')
    num = input('请根据提示输入： ')
    if num == '0':
        registered()
    if num == '1':
        login()
    if num == '2':
        print('欢迎下次使用！')
        flag = False
        return flag

def login():
    name = input('请输入用户名： ')
    if name in database:
        for i in range(3):
            pw = input('请输入密码： ')
            if password[name] == pw:
                login_first(name)
                break
            else:
                continue
    else:
        print('用户不存在请先注册')
        registered()

database = {None:None}
password = {None:None}
data = {'database': database, 'password': password}
flag = True


while flag:
    try:
        with open('ATM_user.pkl', 'rb') as f:
            datas = pickle.load(f)
            database = datas['database']
            password = datas['password']
        while flag:
            main()
        with open('ATM_user.pkl', 'wb') as f:
            # print(datas)
            pickle.dump(datas, f)
    except:
        with open('ATM_user.pkl', 'wb') as f:
            # print(datas)
            pickle.dump(data, f)

