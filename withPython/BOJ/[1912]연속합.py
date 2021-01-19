import sys
N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

res = [0] * N
maxV = -1000

for i in range(N):
    res[i] = max(res[i-1] + arr[i], arr[i])
    maxV = max(maxV, res[i])

print(maxV)