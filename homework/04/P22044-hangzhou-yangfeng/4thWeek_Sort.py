#!/usr/bin/env python
# coding: utf-8

# In[74]:


s = "Sorting123456879AFLdfkgs"

c = []
bigc = []
ns = []
nd = []

length = int(len(s))
for i in range(length):
    if s[i].isalpha() == True:
        if s[i].islower() == True:
            c.append(s[i])
        else:
            bigc.append(s[i])
    else:
        if s[i].isdigit() == True:
            if (int(s[i]) % 2) == 0:
                nd.append(s[i]) 
            else: 
                ns.append(s[i])
print(c,bigc,ns,nd)

newlist = [*c,*bigc,*ns,*nd]
print(newlist)
"""
写的很好，不过有些问题哦
试试 Sorting123456879AFLdfkgs 这个排序
"""
