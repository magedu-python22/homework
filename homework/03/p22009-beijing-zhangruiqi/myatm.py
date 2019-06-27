#-*- encoding=utf-8 -*-

import os
import sys

#注册
def signout(apfile,infodict):
	ac = input("请输入账号：")
	ps = input("请输入密码：")
	ph = input("请输入电话号码：")
	ba = 5000
	if ac in infodict:
		print('账号已存在，请重新注册')
		return 1
	else:
		infodict[ac] = {'password':ps,'phone':ph,'balance':ba}
		f = open(apfile,'w')
		f.write(str(infodict))
		f.close()
		return 0
#功能界面
def loginform(infodict,ac):
	print('----------------------------')
	print('-                          -')
	print('-       1 查看余额         -')
	print('-       2  转 账           -')
	print('-       3  取 款           -')
	print('-       4  存 款           -')
	print('-       5  退 出           -')
	print('-                          -')
	print('----------------------------')
	userinfo = infodict[ac]
	selectnum1 = int(input())
	loggedin(selectnum1,userinfo,infodict,ac)

#登录
def signin(infodict):
	ac = input("请输入账号：")
	ps = input("请输入密码：")
	if ac in infodict and infodict[ac]['password'] == ps:
		loginform(infodict,ac)
	else:
		return 0
#转账
def transfer(infodict,ac):
	ac1 = input('请输入转入账户:')
	if ac1 in infodict:
		ac1info = infodict[ac1]['phone']
		print('转入账户信息为：账号：',ac1,'电话号码：',ac1info)
		tb = int(input('请输入转账金额：'))
		print('是否确认转账？')
		print('    1 确认        2 返回     ')
		selectnum3 = int(input())
		if selectnum3 == 1:
			infodict[ac]['balance'] = infodict[ac]['balance']-tb
			if infodict[ac]['balance']<0:
				print('余额不足！')
				loginform(infodict,ac)
			infodict[ac1]['balance'] = infodict[ac1]['balance']+tb
			f = open(apfile,'w')
			f.write(str(infodict))
			f.close()
			print('转账成功')
			loginform(infodict,ac)


			

#查看余额
#取款 存款
def loggedin(selectnum1,userinfo,infodict,ac):
	if selectnum1 == 1:
		balance = userinfo['balance']
		print('当前余额：',balance)
		print('----------------------------')
		print('-         1 返回           -')
		print('-         2 退出           -')
		print('----------------------------')
		selectnum2 = int(input())
		if selectnum2 == 1:
			loginform(infodict,ac)
		if selectnum2 == 2:
			quit()
	if selectnum1 == 2:
		transfer(infodict,ac)
	if selectnum1 == 3:
		drawmoney = int(input('输入取款金额：'))
		infodict[ac]['balance'] = infodict[ac]['balance']-drawmoney
		print('取款成功')
		f = open(apfile,'w')
		f.write(str(infodict))
		f.close()
		loginform(infodict,ac)
	if selectnum1 == 4:
		depositmoney = int(input('输入存款金额：'))
		infodict[ac]['balance'] = infodict[ac]['balance']+depositmoney
		print('存款成功')
		f = open(apfile,'w')
		f.write(str(infodict))
		f.close()
		loginform(infodict,ac)
	if selectnum1 == 5:
		quit()


#退出
def qiut():
	sys.exit()

#初始界面
def login(apfile,infodict):
	print('-------欢迎使用ATM机-------')
	print('-                         -')
	print('-          1 注册         -')
	print('-                         -')
	print('-          2 登录         -')
	print('-                         -')
	print('-          3 退出         -')
	print('---------------------------')
	selectnum = int(input())
	login1(apfile,infodict,selectnum)
	return selectnum

#登录	
def login1(apfile,infodict,selectnum):
	while selectnum == 1:
		selectnum = signout(apfile,infodict)
		if selectnum == 0:
			login(apfile,infodict)
	while selectnum == 2:
		num = 1
		while num <= 3:
			sinum = signin(infodict)
			if sinum == 0:
				print('请重新输入账号密码')
				num = num+1

		if num > 3:
			print('三次输入机会已经使用完，退出！')
			quit()

	while selectnum == 3:
		qiut()

if __name__=='__main__':
	
	curpath = os.getcwd()
	apfile = os.path.join(curpath,'apfile.txt')
	if os.path.exists(apfile):
		f = open(apfile,'r')
		a = f.read()
		infodict = eval(a)
	else:
		infodict = {}

	login(apfile,infodict)
	





