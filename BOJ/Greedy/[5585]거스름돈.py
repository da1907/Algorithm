pay = int(input())

change = 1000 - pay
coin = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in coin:
    while change >= i:
        cnt += change //i
        change = change % i

print(cnt)