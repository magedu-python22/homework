import re
text = '''foo = 23 + 42 * 10'''
for i,c in enumerate(text, 1):
    print((i-1, c), end='\t' if i%8==0 else ' ')
print()

NAME = '(?P<NAME>fo+)'
EQ = '(?P<EQ>=)'
NUM = '(?P<NUM>\d{2})'
PLUS = '(?P<PLUS>\+)'
TIMES = '(?P<TIMES>\*)'
tokens = []
for i in (NAME,EQ,NUM,PLUS,TIMES):
    regex = re.compile(i)
    matcher = re.findall(i, text)
    if i == NAME:
        print(('NAME',matcher[0]))
        tokens.append(('NAME',matcher[0]))
    if i == EQ:
        print(('EQ', matcher[0]))
        tokens.append(('EQ', matcher[0]))
    if i == NUM:
        print(('NUM', matcher[0]))
        tokens.append(('NUM', matcher[0]))
    if i == PLUS:
        print(('PLUS', matcher[0]))
        tokens.append(('PLUS', matcher[0]))
    if i == NUM:
        print(('NUM', matcher[1]))
        tokens.append(('NUM', matcher[1]))
    if i == TIMES:
        print(('TIMES', matcher[0]))
        tokens.append(('TIMES', matcher[0]))
    if i == NUM:
        print(('NUM', matcher[2]))
        tokens.append(('NUM', matcher[2]))
print(tokens)
print('~~~~~~~~~~~~~~')
tokens[3],tokens[5] = tokens[5],tokens[3]
tokens[4],tokens[6] = tokens[6],tokens[4]
tokens[4],tokens[5] = tokens[5],tokens[4]
print(tokens)
# print(matcher[0],matcher[1])
# print(result)
# print(result.groups())
# print(result.groupdict())

"""
稍微有点小复杂，可以试着在优化下
少个函数的那个，记得补上
"""
