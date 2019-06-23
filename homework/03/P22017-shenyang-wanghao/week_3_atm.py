prompt_username="Please enter your username: "
prompt_username+="\nPlease enter 'q' at any time to quit the program "
prompt_username+="\nNew customer enter 'c' to create an account: "
prompt_password = "Please enter your password: "
prompt_try_again = "Please try angain!"
prompt_new_username = "Your account doesn't exist"
prompt_new_username ="\nPlease register new account with your username:"
prompt_new_password = "Please create your password: "
prompt_contact_info = "Please enter your phone number: "
prompt_func = "Please enter the number to select the function: "
prompt_func += "1. Draw Money. 2. Save Money. 3. Transfer Money "
prompt_amount = "Please enter the amount: "
prompt_others = "Tell me the name you want to transfer: "
pwd_counter = 1

customers = {

			'zhangsan': {
							'password': '123456',
							'phonenumber': 66666666,
							'balance' : 1000000,
						},
			'lisi': { 
							'password': '234567',
							'phonenumber': 88888888,
							'balance': 2000,
					}
			}
customers_new = {}
origin_info = True
while origin_info:
	

	u_u = input(prompt_username)
	u_pwd = ''
	if u_u == 'q':
		origin_info = False
	elif u_u!='q' and u_u!='c':
			u_u in customers.keys()
			u_pwd = input(prompt_password)
			if customers[u_u]['password']!=u_pwd and pwd_counter<3:
				u_pwd = input(prompt_try_again)
				pwd_counter += 1
				if pwd_counter == 3:
					origin_info = False
			elif u_pwd == 'q':
				origin_info = False
			elif customers[u_u]['password']==u_pwd and u_pwd!='q':
				print("Your information shown as follows: "+str(customers[u_u]))
				select_func = input(prompt_func)
				if select_func == 'q':
					origin_info = False	
				elif select_func == '1' and select_func != 'q':
					amount_1 = input(prompt_amount)
					if int(amount_1)>customers[u_u]['balance']:
						print("Your balance is not enough!")
						origin_info = False
					else: 
						customers[u_u]['balance'] -= int(amount_1)
						print("Now you have only " + \
						str(customers[u_u]['balance']) + " left.") 
				elif select_func == '2' and select_func != 'q':
					amount_2 = input(prompt_amount)
					customers[u_u]['balance'] += int(amount_2)
					print("Now you have "+str(customers[u_u]['balance'])+" dollars")
				elif select_func == '3' and select_func !='q':
					others = input(prompt_others)
					if others == 'q':
						origin_info=False 
					amount_3 = input(prompt_amount)
					if amount_3 == 'q':
						origin_info=False 
					customers[u_u]['balance'] -= int(amount_3)
					print("Now you have only " + \
					str(customers[u_u]['balance']) +" left.")
					if others in customers.keys():
						customers[others]['balance'] += int(amount_3)
						print("Now "+others+" get "+str(amount_3)+" dollars")
							

	elif u_u not in customers.keys() or unverified_username=='c': 
		n_username = input(prompt_new_username)
		n_password = input(prompt_new_password)
		contact_info = input(prompt_contact_info)
		if n_username=='q' or n_password=='q' or contact_info=='q':
			origin_info=False
		customers_new[n_username] = {
		'password':n_password,
		'phonenumber':contact_info,
		'balance':5000
		}
		print("\nNow you are awarded 5000 Dollars")

	print("Bye-Bye!")
customers.update(customers_new)


filename = 'customers_infomation.txt'
with open(filename, 'w') as file_object:
	file_object.write(str(customers))

					
"""
1. 新创建用户的时候，登录有些问题哦
2. 没有提供修改密码的功能
3. 逻辑上没有啥太大的问题
"""
			
