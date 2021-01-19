import sys

num = sys.stdin.readline().strip()
num = sorted(num, reverse = True)

if '0' not in num:
    print(-1)
else:
    sum = 0
    for i in num:
        sum += int(i)
    if sum % 3 != 0:
        print(-1)
    else:
        print("".join(num))