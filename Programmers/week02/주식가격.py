def solution(prices):
    result = [0] * len(prices)
    for i in range(len(prices)-1):
        cnt = 0
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                cnt += 1
            else:
                cnt += 1
                break
        result[i] = cnt
    return result

prices = list(map(int,input().split()))
print(solution(prices))