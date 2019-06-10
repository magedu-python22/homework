numlist = list(range(101))
for i in numlist:
    if i == 0:
        continue
    if i % 15 == 0:
        numlist[i] = 'FizzBuzz'
        continue
    if i % 5 == 0:
        numlist[i] = 'Buzz'
        continue
    if i % 3 == 0:
        numlist[i] = 'Fizz'
        continue
print(numlist)
# 这个没有什么问题