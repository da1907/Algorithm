import sys
input = sys.stdin.readline

def compareMax(a, b):
    if abs(a) > abs(b):
        return abs(a)
    else:
        return abs(b)

def getNum(x, r, c):
    minV = ((x-1) * 2 + 1)**2 +1
    maxV = (x*2 + 1) ** 2
    #print(x, minV, maxV)

    if x == abs(r):
        if r > 0:
            return maxV - x - c
        else:
            return minV + (2 * x - 1) + x - c
    else:
        if c > 0:
            return minV + x - r -1
        else:
            return maxV - x * 2 - x - r

def solution(r1, c1, r2, c2):
    max_level = max(abs(r1), abs(c1), abs(r2), abs(c2))
    maxV = compareMax(r1, c1)
    num1 = getNum(maxV, r1, c1)

    maxV = compareMax(r2, c2)
    num2 = getNum(maxV, r2, c2)

    answer = [[0 for _ in range(c2 - c1 + 1)] for _ in range(r2 - r1 + 1)]
    answer[0][0] = num1
    answer[-1][-1] = num2


    print(answer)
    return

r1, c1, r2, c2 = list(map(int, input().split()))
print(solution(r1, c1, r2, c2))