s = 'Sorting1234'
pre = [ord(_) for _ in s]
length = len(pre)

for i in range(length):
    maxindex = i
    for j in range(i+1, length):
        if pre[j] > pre[maxindex]:
            maxindex = j
    if maxindex != i:
        pre[i], pre[maxindex] = pre[maxindex], pre[i]
    if pre[i] < 65:
        state = i
        break

for m in range(state, length):
    if pre[m] % 2:
        continue
    for n in range(m+1, length):
        if pre[n] % 2:
            pre[m], pre[n] = pre[n], pre[m]
            break

cur = [chr(i) for i in pre]
print(cur)
