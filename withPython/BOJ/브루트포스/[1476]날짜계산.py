E, S, M = map(int, input().split())

num = 1
while True:
    if (num-E)%15 == 0 and (num-S)%28 == 0 and (num-M)%19 == 0:
        print(num)
        break
    else:
        num += 1