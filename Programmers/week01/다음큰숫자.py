num = int(input())
ans = 0

biNum = bin(num)
biStr = list(biNum)
biStr.pop(0)
biStr.pop(0)

result = [0] * (len(biStr)+1)

for i in range(len(biStr)-1, -1, -1):
    if biStr[i] == '1':
        for j in range(i-1, -1, -1):
            if biStr[j] == '0':
                biStr[i], biStr[j] = biStr[j], biStr[i]

                for k in range(0, j+1):
                    result[k+1] = biStr[k]
                cnt1 = biStr.count('1')
                cnt2 = result.count('1')
                x = len(biStr)
                for w in range(cnt1 - cnt2):
                    result[x] = 1
                    x -= 1
                for i in range(len(result)):
                    ans += int(result[i]) * 2 ** (len(result) - i - 1)
                print(ans)
                exit()

cnt = biStr.count('1')
result[0], result[1] = 1, 0
x = len(biStr)
for i in range(cnt-1):
    result[x] = 1
    x -= 1
for i in range(len(result)):
    ans += int(result[i]) * 2**(len(result) - i - 1)
print(ans)
