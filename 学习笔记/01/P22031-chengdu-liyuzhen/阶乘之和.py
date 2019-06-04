s = 0
for i in range(1, 101):
    if i % 2:
        s += i
print(s)

a = 0
for i in range(1, 100, 2):
    a += i
print(a)
n = 1
x = 0
for i in range(1, 6):
    n *= i
    x += n
print(n)
print(x)
