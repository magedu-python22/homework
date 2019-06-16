#!/usr/bin/env python
#coding:utf-8
# @author: fulijun
# @date: 2019-06-17
'''
(1)登陆验证：用户输入用户名密码登陆，检测用户名是否存在以及用户名密码是否匹配；用户名密码各有三次输入机会，超过三次系统退出。
(2)菜单界面：登陆成功后显示功能操作界面，输入序号选择对应功能。
(3)用户注册：用户可以输入用户名和密码创建自己的账号，并输入电话号码等信息，如果用户名存在则让用户重新输入用户名。注册后免费赠送5000元余额。
(4)账户管理：用户可以随时查看自己的账户余额。用户可以输入其他账户用户名，实现转账功能；用户名必须存在。用户也可以模拟实现存取款功能。
(5)用户名和密码以及账户信息等必须永久保存。且基于命令行完成，不需要开发GUI界面。
ps:实现方式不限
'''
import os
import sys
import json

def showFuncMenu(menu_dict):
    print('''Personal Banking Services Entrance >>\n
    Please select one of services by follow:\n
    \t1: System login\n\t2: Transfer Accounts\n\t3: Balance query\n\t4: Deposit \n\t5: Draw\n\t6: User Account Register\n\tOther to Quit\n''')
    while True:
        try:
            user_choice = int(input('Enter Service Tag [1-7]:'))
            if user_choice in list(range(1, 7)):
                return menu_dict[user_choice].items()
            return
        except ValueError:
            print('Number only, Try again !')     
        
def getUsersInfo(users_info_file):
    if os.path.isfile(users_info_file) and os.path.getsize(users_info_file):
        with open(users_info_file, 'r') as f1:
            users_info = json.load(f1)
            return users_info
    return {}
        
def reviseUsersInfo(users_info_file, user_data):    
    with open(users_info_file, 'w+') as f2:
        json.dump(user_data, f2, sort_keys=True)
        
def registerVerify(msgs, requiredLen, maxLen):
    while True:
        info = input(msgs).strip()
        realLen = len(info)
        if realLen >= requiredLen:
            if realLen <= maxLen:
                return info
            else:
                print('Too long ! required length range: [{}~{}]'.format(requiredLen, maxLen))
        else:
            print('Too short ! at least {} strings required'.format(requiredLen))

def userRegister(users_info_file):
    print('''Personal Banking Register Entrance >>\n
    Please sign up your information by follow:\n
    \tusername: personal account\n\t  passwd: personal password\n\t \
    Tel: personal phone number\n\t ID_card: personal ID card number\n''')
    while True:
        username = registerVerify('Enter username:', 3, 10)
        user_dict = getUsersInfo(users_info_file)
        if user_dict.get(username):
            print('username exist, Try again!')
        else:        
            break
    passwd = registerVerify('Enter passwd:', 6, 20)
    tel = registerVerify('Enter Tel:', 7, 11)
    id_card = registerVerify('Enter ID_card:', 15, 18)
    user_dict[username] = [passwd, tel, id_card, 5000]
    reviseUsersInfo(users_info_file, user_dict)
    print('New Account Overview\n\t user:{}, Assets: 5000 RMB'.format(username))
    
def loginVerify(users_info_file, *args):
    user_data = getUsersInfo(users_info_file)
    if user_data.get(args[0]):
        if len(args) == 2:
            for user, infos in user_data.items():
                if args[0] == user and args[1] == infos[0]:
                    if infos[-1] == 'evilUser':
                        return 'violent'
                    return 'succeed'
            return user_data
        return args[0]
    
def userLogin(users_info_file, logined_user_list):
    print('''Personal Banking Login Entrance >>\n
    Please Enter your information by follow:\n
    \tusername: personal account\n\tpasswd: personal password\n\t''')
    cnt = 0
    flag = False
    while cnt <= 3:
        if not flag:
            username = input('Enter username:').strip()
            if loginVerify(users_info_file, username) == username:
                cnt = 0
                flag = True
            else:
                print('Please check if your username is correct, then you have {} times chance to retry'.format(3 - cnt))
                cnt += 1 
            if cnt > 3:
                return 'violent'
        else:
            passwd = input('Enter password:').strip()
            auth_res = loginVerify(users_info_file, username, passwd)
            if auth_res == 'succeed':
                print('Dear {}, Welcome to login Personal Banking System.'.format(username))
                cur_logined_user = logined_user_list.append(username)
                if not cur_logined_user:
                    cur_logined_user = (username)
                return cur_logined_user
            elif auth_res == 'violent':
                print('Dear {}, Your account has locked already, please contact our custom service !'.format(username))
                return 'violent'
            if cnt >= 3:
                if auth_res[username][-1] != 'evilUser':
                    auth_res[username].append('evilUser')
                    reviseUsersInfo(users_info_file, auth_res)
                return 'violent'
            print('[WARN] Password wrong, your account {} will be locked after retry {} times'.format(username, 3 - cnt))
            cnt += 1

def loginedUserVerify(logined_user_list):
    try: 
        cur_logined_user = logined_user_list[-1]      
    except IndexError:
        cur_logined_user = userLogin(users_info, logined_user_list)
    return cur_logined_user

def accountQuery(users_info_file, logined_user_list):
    cur_logined_user = loginedUserVerify(logined_user_list)           
    if cur_logined_user != 'violent':
        cur_user_balance = getUsersInfo(users_info_file)[cur_logined_user][-1]  
        print('\n ======= Account Balance Overview =======\n\t user:{}, Assets: {} RMB\n\n'.format(cur_logined_user, cur_user_balance))
    else:
        print('\n[Notice] Your account might be locked or not exist, please contact our custom service !\n')
    
def accountTransfer(users_info_file, logined_user_list):
    cur_logined_user = loginedUserVerify(logined_user_list) 
    if cur_logined_user != 'violent':
        flag = False
        cnt = 0
        while True:
            if not flag:
                transfered_user = input('Please enter the username you want to transfer:').strip()
                getTransUser_info = loginVerify(users_info_file, transfered_user)
                if transfered_user != getTransUser_info:
                    print('The user {} that you are transferred does not exist'.format(transfered_user))
                    cnt += 1
                elif cur_logined_user == transfered_user:
                    print("[WARN] The same account can't be transferred.")
                else:
                    flag = True
                if cnt >= 3:
                    print('Your operator exceed max retry !')
                    break
            else:
                user_data = getUsersInfo(users_info_file)
                cur_user_balance = user_data[cur_logined_user][-1]
                transed_user_balance = user_data[transfered_user][-1]
                try:
                    transed_wealth = int(input('Enter the amount of money you want to transfer >>'))
                    if transed_wealth > cur_user_balance:
                        print('Sorry, Not sufficient funds, Try again ！')
                    else:
                        break
                except ValueError:
                    print('Number only, Try again ！')
        if cnt < 3:            
            user_data[cur_logined_user][-1] = cur_user_balance - transed_wealth
            user_data[transfered_user][-1] = transed_user_balance + transed_wealth
            reviseUsersInfo(users_info_file, user_data)
            print('\n ======= Account Balance Overview =======\n\t user:{}, Assets: {} RMB\n\n'.format(cur_logined_user, getUsersInfo(users_info_file)[cur_logined_user][-1]))  
            print('\n ======= Account Balance Overview =======\n\t user:{}, Assets: {} RMB\n\n'.format(transfered_user, getUsersInfo(users_info_file)[transfered_user][-1])) 
    else:
        print('\n[Notice] Your account might be locked or not exist, please contact our custom service !\n')     

def drawOrDeposit(msg, users_info_file, logined_user_list):
    cur_logined_user = loginedUserVerify(logined_user_list) 
    if cur_logined_user != 'violent':
        while True:
            try:
                wealth = int(input('Please enter the amount of money you want to {}:'.format(msg)))
                if wealth > 0:
                    break
                else:
                    print('Sorry, Input Error, positive numbe only, Try again ！')
            except ValueError:
                print('Number only, Try again ！')
        user_data = getUsersInfo(users_info_file)
        cur_user_balance = user_data[cur_logined_user][-1]
        if msg == 'deposit':
            user_data[cur_logined_user][-1] = cur_user_balance + wealth
        elif msg == 'draw':
            user_data[cur_logined_user][-1] = cur_user_balance - wealth
        else:
            print('Unkown operate !')
        reviseUsersInfo(users_info_file, user_data)
        print('\nsucceed !\n ======= Account Balance Overview =======\n\t user:{}, Assets: {} RMB\n\n'.format(cur_logined_user, getUsersInfo(users_info_file)[cur_logined_user][-1])) 
    else:
        print('\n[Notice] Your account might be locked or not exist, please contact our custom service !\n') 
            
def accountDeposit(users_info_file, logined_user_list):
    drawOrDeposit('deposit', users_info_file, logined_user_list)

def accountDraw(users_info_file, logined_user_list):
    drawOrDeposit('draw', users_info_file, logined_user_list)

if __name__ == '__main__':
    cur_dir = os.path.dirname(__file__)
    users_info = os.path.join(cur_dir, 'users_info.json')
    logined_user = []

    menu_dict = {1:{userLogin:(users_info, logined_user)}, 
                 2:{accountTransfer:(users_info, logined_user)}, 
                 3:{accountQuery:(users_info, logined_user)},
                 4:{accountDeposit:(users_info, logined_user)},
                 5:{accountDraw:(users_info, logined_user)},
                 6:{userRegister:(users_info,)}
                 }

    while True:
        get_user_decision = showFuncMenu(menu_dict)
        if not get_user_decision:
            print('Thanks for your visiting, Welcome to our online services next time.')
            break
        for bank_func, args in get_user_decision:
            bank_func(*args)
            affirm_msg = input('Back to function menu [y|n] >>')
            if affirm_msg == 'n' or affirm_msg == 'no':
                sys.exit('Quit ...')
            elif affirm_msg == 'y' or affirm_msg == 'yes':
                break
            else:
                print('Operation is not permited !')
                