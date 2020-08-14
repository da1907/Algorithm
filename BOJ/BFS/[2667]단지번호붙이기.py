import sys

def solve(x, y):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if not visited[nx][ny] and board[nx][ny] == 1:
                cnt += 1
                solve(nx, ny)
    return cnt

dx, dy = [0,0,-1,1], [1,-1,0,0]
n = int(sys.stdin.readline())
board, danji = [], []
visited = [[0] * n for _ in range(n)]
cnt = 1

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))

for i in range(n):
    for j in range(n):
        if not visited[i][j] and board[i][j] == 1:
            danji.append(solve(i, j))
            cnt = 1
danji = sorted(danji)
print(len(danji))

for i in danji:
    print(i)
