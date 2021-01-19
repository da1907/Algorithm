import sys

l, c = map(int, sys.stdin.readline().split())
alpha = list(sys.stdin.readline().split())

alpha = sorted(alpha)
mo, ja = [], []
tmp, listed = [], []
num = l - 3

for i in alpha:
    if i == 'a' or i=='e' or i=='i' or i=='o' or i=='u':
        mo.append(i)
    else:
        ja.append(i)

for i in mo:
    for j in ja:
        for k in ja:
            if j == k:
                continue
            tmp.append([i,j,k])
for i in range(len(tmp)):
    tmp[i] = ''.join(tmp[i])

for i in tmp:
    sub = [j for j in alpha if j not in i]
    while num >= 0:
        for k in sub:
            i = i + k
            listed.append(i)
            i = i[0:-1]

for i in range(len(listed)):
    listed[i] = sorted(listed[i])
for i in range(len(listed)):
    listed[i] = ''.join(listed[i])
listed = list(set(listed))
listed = sorted(listed)

for i in listed:
    print(i)
