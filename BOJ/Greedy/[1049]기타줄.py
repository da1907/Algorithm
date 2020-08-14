import sys
line, brand = map(int, sys.stdin.readline().split())
price = []
minV = 1000

for i in range(brand):
    price.append(list(map(int, sys.stdin.readline().split())))

for i in price:
    if i[0] > (i[1] * 6):
        i[0] = i[1] * 6

price = sorted(price, key = lambda price: price[0])
bundle = line // 6
minV = bundle * price[0][0]

tmp = (bundle + 1) * price[0][0]

price = sorted(price, key = lambda price: price[1])
minV += (line % 6) * price[0][1]
minV = min(minV, tmp)

print(minV)