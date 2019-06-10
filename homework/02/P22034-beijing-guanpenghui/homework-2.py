# define list
list3=''
list5=''
list15=''
listelse=''
#cycle
for dividendnum in range(101):
    if dividendnum % 3 == 0:
        list3 = list3 + str(dividendnum)+','
    if dividendnum % 5 == 0:
        list5 = list5 + str(dividendnum)+','
    if dividendnum % 15 == 0:
        list15 = list15 + str(dividendnum)+','
    if dividendnum % 3 !=0 and dividendnum % 5 != 0:
        listelse = listelse + str(dividendnum)+','
print(list3 + 'Fizz' + ',' + list5 + 'Buzz' + ',' + list15 + 'FizzBuzz' + ',' + listelse)
#print(list5 + 'Buzz')
#print(list15 + 'Buzz')
#print(listelse)

# 有问题哦