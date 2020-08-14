import sys
from collections import deque

def check(board):
    cnt0 = 0
    for i in range(n):
        for j in range(m):
            if board[i][j] == 0:
                cnt0 += 1

    if cnt0 > 0:
        return False
    return True


def solve(x, y):
    print(x, y)
    queue = deque()
    queue.append((x, y))
    print(queue)
    while queue:
        x, y = queue.pop()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0:
                print("nx ny", nx, ny)
                board[nx][ny] = board[x][y] + 1
                print(board)
                queue.append((nx, ny))
    return board


m, n = map(int, sys.stdin.readline().split())
board = []
res,cand = [], []
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
visited = [[0] * m for _ in range(n)]
cnt, maxV = 0, 0
flag1, flag2 = False, False

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 1 and not visited[i][j]:
            cand.append
            res = solve(i, j)

for i in range(n):
    for j in range(m):
        maxV = max(maxV, board[i][j])
        print(maxV)

if check(board):
    print(maxV-1)
else:
    print(-1)

