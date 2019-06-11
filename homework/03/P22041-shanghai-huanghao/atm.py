users = {'user1':['111111', 5000], 'user2':['123456', 10000]}

def register(): #用户注册
	username = input('Please enter a user name.\n')
	while username in users:
		username = input('User name already exists!\n')
	users[username] = [None, 5000]
	password = input('Please enter a password.\n')
	while len(password) < 6:
		password = input('The password is too short!\nPassword: ')
	users[username][0] = password
	print('Register Successful!\n')
	return True

def login(): #用户登录
	username = input('User Name: ')
	while username not in users:
		username = input('User name not exists!\nUser Name: ')
	password = input('Password: ')
	count = 0
	while users[username][0] != password:
		password = input('Wrong Password!\nPassword: ')
		count += 1
		if count == 3:
			return False
	print('Log In Successful!\n')
	return username

def query_balance(username): #查询余额
	balance = users[username][1]
	return balance

def transfer(from_user, to_user, amount): #转账
	if amount > users[from_user][1]:
		return False
	else:
		users[from_user][1] -= amount
		users[to_user][1] += amount
		return True

def desposit(username, amount): #存款
	users[username][1] += amount
	return True

def withdraw(username, amount): #取款
	if users[username][1] < amount:
		return False
	else:
		users[username][1] -= amount
		return True

while True:
	print('Enter 1 to register / Enter 2 to login')
	t1 = input('>>> ')
	if t1 == '1':
		register()
		continue
	elif t1 == '2':
		username = login()
		while True:
			if username != False:
				print('1: Query Balance')
				print('2: Transfer')
				print('3: Desposit')
				print('4: Withdraw')
				print('5: Log Out')
				t2 = input('>>> ')
				
				if t2 == '1':
					balance = query_balance(username)
					print(f'Your balance is {balance}.')
					input('Enter anything to continue: ')
					continue
				
				elif t2 == '2':
					print('Transfer To:')
					to_user = input('>>> ')
					if to_user not in users:
						print('User not exists!\n')
						continue
					print('Transfer Amount:')
					transfer_amount = int(input('>>> '))
					if transfer(username, to_user, transfer_amount):
						print('Transfer Successful!')
						print(f'Your balance is {users[username][1]} now.\n')
						input('Enter anything to continue: ')
						continue
					else:
						print('Lack of balance!\n')
						continue

				elif t2 == '3':
					desposit_amount = int(input('Amount: '))
					desposit(username, desposit_amount)
					print('Desposit Successful.\n')
					continue

				elif t2 == '4':
					withdraw_amount = int(input('Amount: '))
					if withdraw(username, withdraw_amount):
						print('Withdraw Successful\n')
						continue
					else:
						print('Lack of balance!\n')
						continue

				elif t2 == '5':
					break

				else:
					print('Please enter a correct number!\n')