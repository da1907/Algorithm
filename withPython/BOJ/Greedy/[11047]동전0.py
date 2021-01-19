import sys

N, K = map(int, sys.stdin.readline().split())
coin = []
cnt = 0

for i in range(N):
    coin.append(int(sys.stdin.readline()))

# def solve(total):
#     global cnt
#     for i in range(N - 1, -1, -1):
#         if coin[i] <= total:
#             total -= coin[i]
#             cnt += 1
#             return total

def solve02(total):
    global cnt
    for i in range(N - 1, -1, -1):
        if coin[i] <= total:
            cnt += total // coin[i]
            print(total)
            total = total % coin[i]
            return total

while K >= coin[0]:
    K = solve02(K)

print(cnt)