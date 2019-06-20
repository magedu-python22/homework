#s = "Sorting1234" 
#给定一个只包含大小写字母，数字的字符串，对其进行排序，保证：
#1 所有的小写字母在大写字母前面
#2 所有的字母在数字前面
#3 所有的奇数在偶数前面 


s = 'cGA9aF1B2345d60'
lowerlist = []
upperlist = []
oddlist = []
evenlist = []
for i in s :
    if i.islower():
        lowerlist.append(i)
    elif i.isupper():
        upperlist.append(i)
    elif int(i) % 2 == 0:
        evenlist.append(i)
    else:
        oddlist.append(i)

lowerlist.sort()
upperlist.sort()
oddlist.sort()
evenlist.sort()
ret = lowerlist + upperlist + oddlist + evenlist
print("".join(ret))