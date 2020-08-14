def plus_123(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    elif n == 3:
        return 4
    else:
        return plus_123(n-1) + plus_123(n-2) + plus_123(n-3)

for i in range(int(input())):
    num = int(input())
    answer = plus_123(num)
    print(answer)