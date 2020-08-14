W, M, I = map(int, input().split())
cnt = 0
num = W + M - I

while num > 0:
    if W > 0:
        W -= 2
    else:
        break

    if M > 0:
        M -= 1
    else:
        break

    num -= 3
    if num >= 0:
        cnt += 1
    else:
        break

print(cnt)