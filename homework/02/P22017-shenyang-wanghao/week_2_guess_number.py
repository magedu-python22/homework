prompt = "\nPlease enter a number, then compare with the embeded number\
and feedback the result to you:"
prompt += "\n(Please enter 'q' to exit the program at any time) "
			
origin_input = True
while True:
	input_number = input(prompt)
	if input_number == 'q':
		break
	elif int(input_number) < 100:
		print("\nYour number less than target, please try again")
	elif int(input_number) > 100:
		print("\nYour number greater than target, please try again\n")
	elif int(input_number) == 100:
		print("\nCongratulations! You are right!")
		break
	
