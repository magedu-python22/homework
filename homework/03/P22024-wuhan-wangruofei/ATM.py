# 银行ATM机系统
# 功能如下
# (1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
# (2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
# (3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
# (4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
# (5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
# 文件夹下account.txt内保存用户的用户名、密码和余额信息
# 每行的信息分别是username,cards,password,IDNum,tel,vacancies
import os
import random
import getpass
#用户登录
def show():
    print("选择您要办理的业务")
    print("1.查询余额".center(60,'='))
    print("2.转账汇款".center(60,'='))
    print("3.存款".center(60,'='))
    print("4.取款".center(60,'='))
    print("5.退出".center(60,'='))
#用户注册
def signup():
    print("用户注册".center(60,' '))
    fp = open('account.txt', 'r')
    size=os.path.getsize('account.txt')#判断文件是否为空
    USERS=fp.readlines()
    fp.close()
    fp = open('account.txt', 'a+')
    username=input("用户名>>> ")
    putin=[]
    while True:
        password = input("密码>>> ")
        confirm = input("确认密码>>> ")
        IDNum=input("请输入身份证号>>> ")
        if not IDNum.isdigit():
            break
        tel=input("请输入电话号码>>> ")
        if not tel.isdigit():
            break

        if (password == confirm) and (len(IDNum) == 18) and (len(tel) == 11):
            # 判断两次输入的密码是否相同，判断身份证号和手机号是否合法
            print("注册成功，到柜台取卡".center(30, ' '))
            break

#随机分配一个卡号，并防止生成重复的卡号
    repeat=False
    nums=0
    while True:
        nums = random.randint(6217850000000000000, 6217859999999999999)
        for i in range(len(USERS)):
            l=USERS[i].split(' ')
            if str(nums) in l:
                repeat = True
                break
        if not repeat:
            break
    cardsID = str(nums)
#注册成功送5000余额
    userstr=' '.join([username,cardsID,password,IDNum,tel,'5000'])
    if size==0:
#如果是空文件，直接写入
        putin = [userstr]
    else:
#如果不是空文件，先换行再写入
        putin=['\n',userstr]
    fp.writelines(putin)
    fp.close()
#返回注册的信息，免去再次登录的麻烦
    return userstr.split(' ')
def signin():
    fp = open('account.txt', 'r')
    USERS=fp.readlines()
    count = 0
    List1=[]
    putin = input("请输入卡号>>> ")
    pas = input("请输入密码>>> ")
    for i in range(len(USERS)):
        List1 = USERS[i].split(' ')
        if (putin in List1) and (pas in List1):
            fp.close()
            return List1
    return []
def searchuse():
    fp = open('account.txt', 'r')
    USERS = fp.readlines()
    putin = input("请输入卡号>>> ")
    for i in range(len(USERS)):
        List1 = USERS[i].split(' ')
        if putin in List1:
            fp.close()
            return List1
    print('不存在该用户，请检查卡号')
def overage(List1):
    # 查询余额，输入登录后的信息列表
    return int(List1[-1].strip('\n'))
#转账
def transfer(List1,List2,over1,over2):
    fp = open('account.txt', 'r', encoding='utf-8')
    USERS = fp.readlines()
    fp.close()
    r = 0
    l = 0
    for i in range(len(USERS)):
        if List1 == USERS[i].split(' '):
            r = i
        elif List2 == USERS[i].split(' '):
            l = i
        else:
            continue
    fp = open('account.txt', 'w',encoding='utf-8')
    sum=int(input("请输入转账金额>>> "))
    if sum>over1:
        print("余额不足")
        fp.close()
        return
    else:
        num1=over1-sum
        num2=over2+sum
        if List1[-1].endswith('\n'):
            List1[-1]="{}{}".format(str(num1),'\n')
        else:
            List1[-1]="{}".format(str(num1))
        if List2[-1].endswith('\n'):
            List2[-1]="{}{}".format(str(num2),'\n')
        else:
            List2[-1]="{}".format(str(num2))
        USERS[r]=' '.join(List1)
        USERS[l]=' '.join(List2)
        fp.writelines(USERS)
        fp.close()
#存款
def deposit(List):
    fp = open('account.txt', 'r', encoding='utf-8')
    USERS = fp.readlines()
    fp.close()
    r=0
    for i in range(len(USERS)):
        if List == USERS[i].split(' '):
            r = i
            break
    dep=int(input("请输入存款金额>>> "))
    if dep>20000:
        fp.close()
        print("单笔存款超过20000元请到柜台")
    else:
        fp = open('account.txt', 'w', encoding='utf-8')
        ovr=overage(List)+dep
        if List[-1].endswith('\n'):
            List[-1]="{}{}".format(str(ovr),'\n')
        else:
            List[-1]="{}".format(str(ovr))
        USERS[r]=' '.join(List)
        fp.writelines(USERS)
        fp.close()
        print("存款成功")
#取款
def withdraw(List):
    fp = open('account.txt', 'r', encoding='utf-8')
    USERS = fp.readlines()
    fp.close()
    r = 0
    for i in range(len(USERS)):
        if List == USERS[i].split(' '):
            r = i
            break

    dep = int(input("请输入取款金额>>> "))
    if dep > 20000:
        print("单笔取款超过20000元请到柜台")
    elif dep>overage(List):
        print("余额不足")
    else:
        fp = open('account.txt', 'w', encoding='utf-8')
        ovr = overage(List) - dep
        if List[-1].endswith('\n'):
            List[-1] = "{}{}".format(str(ovr), '\n')
        else:
            List[-1] = "{}".format(str(ovr))
        USERS[r] = ' '.join(List)
        fp.writelines(USERS)
        fp.close()
        print("取款成功")
def main():
    """
    菜单界面显示
    """
    print("中国银行自主存取系统".center(60, '='))
    print("登录/注册".center(60,' '))
    List_1=[]
    sign = input("登录？[Y/n]:")
    if sign == 'Y':
        count = 0
        while True:
            count += 1
            if count < 4:
                List_1 = signin()
                if List_1:
                    print("登录成功")
                    break
            else:
                print("请先注册")
                List_1 = signup()
    else:
        List_1 = signup()
    over=0
    while True:
        show()
        business = int(input(">>> "))
        if business == 1:
            print("余额为{}".format(overage(List_1)))
        elif business == 2:
            over1 = overage(List_1)
            List_2=searchuse()
            over2=overage(List_2)
            transfer(List_1,List_2,over1,over2)
        elif business == 3:
            deposit(List_1)
        elif business == 4:
            withdraw(List_1)
        else:
            print("业务办理完成，请取走您的卡")
            break
if __name__=='__main__':
    main()

"""
1.逻辑没有什么问题
2.写的很不错
3.注释的话 可以写到函数里面,类似main里面的
"""