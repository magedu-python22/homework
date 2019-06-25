def sortl(s):
    xiaoxie=[]
    daxie=[]
    jishu=[]
    oushu=[]
    for i in s:
        if i.isalpha() == True:
            daxie.append(i) if i.isupper() == True else xiaoxie.append(i)
        else:
            jishu.append(i) if int(i) % 2 ==1 else oushu.append(i)

    d=sorted(xiaoxie)+sorted(daxie)+sorted(jishu)+sorted(oushu)
    return ("".join(map(str,d)))
m = "Sorting1234"
print(sortl(m))
"""
棒，
"""
