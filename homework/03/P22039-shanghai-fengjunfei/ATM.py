#初始化数据
import json
Userinfo = {'fengjunfei':{'passwd':'123456','phone':'18688888888','money':3000},'feng':{'passwd':'123456','phone':'18611111','money':8000}}
with open('/tmp/atm_userinfo.json','w',encoding='utf-8') as f:
    f.write(json.dumps(Userinfo,ensure_ascii=False,indent=4))

#正式代码
import json

def read_atm_userinfo():
    f = open('/tmp/atm_userinfo.json','r')
    Userinfo = json.load(f)

def write_atm_userinfo():
    with open('/tmp/atm_userinfo.json','w',encoding='utf-8') as f:
        f.write(json.dumps(Userinfo,ensure_ascii=False,indent=4))

###用户登录
def Userlogin():
    global Userflag
    global username
    global passwd
    Userflag = False
    count = 3
    while Userflag is False and count > 0:
        read_atm_userinfo()
        print('-'*25)
        print()
        print ('{:^22}'.format('请输入账户信息'))
        username = input('用户名:  ')
        if username not in Userinfo:
            print('\n用户名不存在！！！')
            count -= 1
            print('你还有 {} 次机会'.format(count))
            continue
        passwd = input('密码:    ')
        if passwd != Userinfo[username]['passwd']:
            print('\n输入密码有误！！！')
            count -= 1
            print('你还有 {} 次机会'.format(count))
            continue
        Userflag = True
        continue

###用户注册
def Register():
    global username
    global passwd
    Registerflag = False
    while not Registerflag:
        read_atm_userinfo()
        print('-'*25)
        print()
        print ('{:^22}'.format('请输入注册账户信息'))
        username = input('用户名: ')
        if username in Userinfo:
            print('\n用户名已经存在！')
            continue
        passwd = input('密码:   ')
        phone = input('手机号:  ')
        Userinfo[username] = {'passwd':passwd,'phone':phone,'money':'5000'}
        write_atm_userinfo()
        Registerflag = True
        print('\n恭喜你注册成功,获得5000元,即将返回登录页')

###查询余额
def select_action():
    print('\n你的账户余额为 {} 元'.format(Userinfo[username]['money']))

###存钱
def add_action():
    add_amount = int(input('请输入你要存的金额'))
    Userinfo[username]['money']=int(Userinfo[username]['money']) + add_amount
    print('\n你存入 {} 元，现在账户余额为 {} 元'.format(add_amount,Userinfo[username]['money']))
    write_atm_userinfo()

###取钱
def reduce_action():
    reduce_actionflag = True
    while reduce_actionflag :
        reduce_amount = int(input('请输入你要取的金额'))
        if reduce_amount > int(Userinfo[username]['money']):
            print('\n你账户中的金额不足,你只有 {} 元'.format(Userinfo[username]['money']))
            continue
        reduce_actionflag = False
        Userinfo[username]['money']=int(Userinfo[username]['money']) - reduce_amount
        print('\n你取出来 {} 元，账户剩余 {} 元'.format(reduce_amount,Userinfo[username]['money']))
        write_atm_userinfo()

###转账
def transfer_action():
    """
    转账
    :return:
    """
    Dst_usernameflag = False
    while not Dst_usernameflag:
        read_atm_userinfo()
        print('-'*25)
        print()
        print ('{:^22}'.format('请输入转账目标用户名'))
        dst_username = str(input('\n用户名: '))
        if dst_username not in Userinfo:
            print('\n用户名不存在！')
            break
        Dst_usernameflag = True
        dst_amount = int(input('\n请输入你要转的金额'))
        if dst_amount > int(Userinfo[username]['money']):
            print('\n你账户中的余额不足,你只有 {} 元'.format(Userinfo[username]['money']))
            break
        Userinfo[username]['money']=int(Userinfo[username]['money']) - dst_amount
        Userinfo[dst_username]['money']=int(Userinfo[dst_username]['money']) + dst_amount
        print('\n你转给 {}  {} 元，自己账户剩余 {} 元'.format(dst_username,dst_amount,Userinfo[username]['money']))
        write_atm_userinfo()

def memu_login():
    print('\n欢迎登录XX银行ATM机系统')
    print()
    print('   编号        操作')
    print('     1       用户登录')
    print('     2       用户注册')
    print('     3         退出')

def memu_action():
    print('\n欢迎登录XX银行ATM机系统')
    print()
    print('   编号        操作')
    print('     1       查询余额')
    print('     2         存钱')
    print('     3         取钱')
    print('     4         转账')
    print('     5      返回上一级')

while True:
    memu_login()
    num = input('请输入你要操作的标号')
    if num in ['1','2','3']:
        if num == '1':
            Userlogin()
            if Userflag == False:
                print('\n你已经输错三次，已经退出系统！！！')
                break
            print('\n登录成功')
            print()
            actionflag = True
            while actionflag:
                memu_action()
                num = input('请输入你要操作的标号')
                if num in ['1','2','3','4','5']:
                    if num == '1':
                        select_action()
                    elif num == '2':
                        add_action()
                    elif num == '3':
                        reduce_action()
                    elif num == '4':
                        transfer_action()     
                    else:
                        actionflag = False
                        continue
                else:
                    print('\n输入有误，请稍后重试')
            continue
        elif num == '2':
            Register()
            continue
        else:
            print('你已退出')
            break
        break
    else:
        print('输入有误，请稍后重试！')

"""
1.注释参考下 transfer_action 这个里面的写法
2.170行的break的是做什么用的？
3.用户文件忘记上传了吧
4.逻辑上没有太大的问题 
"""