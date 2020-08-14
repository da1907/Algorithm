import sys

N, M = map(int, sys.stdin.readline().split())
A = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
B = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
flag = [[0] * M] * N
cnt = 0

def flip(x, y):
    for i in range(x, x+3):
        for j in range(y, y+3):
            A[i][j] = 1 - A[i][j]

def check():
    for i in range(N):
        for j in range(M):
            if A[i][j] != B[i][j]:
                return 0
    return 1

for i in range(0, N-2):
    for j in range(0, M-2):
        if A[i][j] != B[i][j]:
           flip(i, j)
           cnt += 1

if check():
    print(cnt)
else:
    print(-1)


