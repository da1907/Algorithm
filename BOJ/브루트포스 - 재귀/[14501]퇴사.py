import sys

def solve(n, T, P):
    dp = [0 for i in range(n)]

    #초기값
    #마지막 날은 1일간만 상담해야 들어갈 수 있음
    if T[n-1] == 1:
        dp[n-1] = P[n-1]

    #뒤에서부터 계산
    for i in range(n-2, -1, -1):
        day = i + T[i]

        if day == n:    #상담 가능일이 n이랑 똑같으면 이후에는 상담 불가능
            dp[i] = max(P[i], dp[i+1])

        elif day < n:   #상담 가능일이 n보다 작으면 이후 상담 가능
            dp[i] = max(P[i] + dp[day], dp[i+1])
        elif day > n:
            dp[i] = dp[i+1]

    print(dp[0])

n = int(sys.stdin.readline())
T, P = [], []

for i in range(n):
    Ti, Pi = map(int, sys.stdin.readline().split())
    T.append(Ti)
    P.append(Pi)

solve(n, T, P)