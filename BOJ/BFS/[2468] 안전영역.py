import sys
from copy import deepcopy
from sys import setrecursionlimit
setrecursionlimit(10**6)

def solution(x, y):
    if not visited[x][y]:
        visited[x][y] = 1
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<n and tmp[nx][ny]:
                solution(nx, ny)
    return

dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(sys.stdin.readline())
board = []

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

maxV = 0
cnt,ans = 0, 0

for i in range(n):
    for j in range(n):
        maxV = max(maxV, board[i][j])

for k in range(0, maxV+1):
    cnt = 0
    visited = [[0] * n for _ in range(n)]

    tmp = deepcopy(board)

    for i in range(n):
        for j in range(n):
            if tmp[i][j] <= k:
                tmp[i][j] = 0
    for i in range(n):
        for j in range(n):
            if tmp[i][j] and not visited[i][j]:
                solution(i, j)
                cnt += 1
    ans = max(cnt, ans)

print(ans)