import sys

n, m = map(int, sys.stdin.readline().split())

if n == 1:
    print(1)
elif n == 2:
    if m >= 7:
        print(4)
    else:
        print((m+1)//2)
else:
    if m >= 7:
        print(m - 2)
    elif m == 1:
        print(1)
    elif m == 2:
        print(2)
    elif m == 3:
        print(3)
    else:
        print(4)
