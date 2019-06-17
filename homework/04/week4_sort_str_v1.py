# Sorting in sequence: Lower letter, upper letter, number, odd, even
s = "Sorting1234"


tmp_lower = ''
tmp_upper = ''
tmp_odd = ''
tmp_even = ''
for i in range(len(s)):
	if s[i].islower():
		tmp_lower = tmp_lower + s[i]
		
	elif s[i].isupper():
		tmp_upper = tmp_upper + s[i]
		
	elif int(s[i])%2 != 0:
		tmp_odd = tmp_odd + s[i]
		
	elif int(s[i])%2 == 0:
	    tmp_even = tmp_even + s[i]
	    
	
s = tmp_lower+tmp_upper+tmp_odd+tmp_even
print(s)
	
	
	
