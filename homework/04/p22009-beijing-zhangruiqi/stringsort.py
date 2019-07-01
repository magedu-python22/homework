s = input("请输入字符串：")
numlist = ['1','2','3','4','5','6','7','8','9','0']

odcapitallist = []
evenlist = []
zlist = []
for i in s:
    if i in numlist:
        if int(i)%2==0:
            evenlist.append(i)
        else:
            odcapitallist.append(i)
    else:
        zlist.append(i)

for i in range(len(evenlist)-1):
    for j in range(i+1,len(evenlist)):
        if int(evenlist[i]) > int(evenlist[j]):
            evenlist[i],evenlist[j] = evenlist[j],evenlist[i]

for i in range(len(odcapitallist)-1):
    for j in range(i+1,len(odcapitallist)):
        if int(odcapitallist[i]) > int(odcapitallist[j]):
            odcapitallist[i],odcapitallist[j] = odcapitallist[j],odcapitallist[i]


j1 = "".join(odcapitallist+evenlist)
capitallist = []
lowercaselist = []
for z in zlist:
    if z.islower():
        lowercaselist.append(z)
    else:
        capitallist.append(z)
capitallist.sort()
lowercaselist.sort()
d = "".join(capitallist)
x = "".join(lowercaselist)
print(x+d+j1)
