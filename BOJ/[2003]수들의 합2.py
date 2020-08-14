N, M = map(int, input().split())
nums = list(map(int, input().split()))
cnt = 0
sums = [0] * (N + 1)

for n in range(1, N+1):
    sums[n] = sums[n-1] + nums[n-1]

for i in range(len(sums)):
    if sums[i] >= M:
        for j in range(i):
            if sums[i] - sums[j] == M:
                cnt += 1

print(cnt)