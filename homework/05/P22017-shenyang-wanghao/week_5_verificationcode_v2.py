import random

v_code = [0]*6
elements = {}
chr(random.randint(65, 90))
random.randint(0, 255)
def verification_code(element_number):
	"""create the verification code"""
	for i in range(0, element_number):

		element = {chr(random.randint(65, 90)):[random.randint(0,255),random.randint(0,255),random.randint(0,255)]}
		v_code[i] = element
	
	print(v_code)
	
verification_code(6)
