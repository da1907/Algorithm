import sys

prices = []

prices = list(map(int, sys.stdin.readline().split()))
duration = [0] * len(prices)

def solution(prices):
    for i in range(len(prices)):
        for j in range(i+1, len(prices)):
            if prices[i] <= prices[j]:
                duration[i] += 1
            elif prices[i] > prices[j]:
                duration[i] += 1
                break
    return duration

print(solution(prices))

