import sys

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
res = [0] * N
ans = []
for i in range(1, N+1):
    num = arr[i-1]
    cnt = 0
    for j in range(N):
        if res[j] == 0 and cnt == num:
            res[j] = i
            break
        if res[j] == 0:
            cnt += 1

#print(*res)
ans[1] = 4