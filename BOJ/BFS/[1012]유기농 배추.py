import sys

T = int(sys.stdin.readline())
M, N, K = map(int, sys.stdin.readline().split())
pos = []
cnt = 0
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
board = [[0 for _ in range(M)]] * N
visited = [[0 for _ in range(M)]] * N

for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    board[y][x] = 1

def bfs(start, board):
    global cnt
    visited[x][y] = 1
    for i in range(4):
        tmp_x = x + dx[i]
        tmp_y = y + dy[i]
        print("x y", tmp_x, tmp_y)
        if (x < 0 or x >= M) and (y < 0 or y >= N):
            continue
        if (board[tmp_x][tmp_y] == 1) and (not visited[tmp_x][tmp_y]):
                print("<<<")
                bfs(tmp_x, tmp_y)
    cnt += 1
    return pos


for y in range(N):
    for x in range(M):
        if board[y][x] == 1:
            cnt += bfs((y,x), board)

print(cnt)