import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
board = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip())))
visited = [[0] * m for _ in range(n)]

queue = deque()
queue.append((0, 0))
visited[0][0] = 1
while queue:
    x, y = queue.popleft()
    if x == n-1 and y == m-1:
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m and board[x][y] == 1:
            if not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                queue.append((nx, ny))

print(visited[n-1][m-1])
