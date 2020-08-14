import sys
sys.setrecursionlimit(10**8)

def bfs(x, y, cnt):
    matrix[x][y] = 0
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0<=nx<n and 0<=ny<m and matrix[nx][ny]:
            bfs(nx, ny, cnt)
    return cnt+1

T = int(sys.stdin.readline())
for i in range(T):
    m, n, k = map(int, sys.stdin.readline().split())

    dx, dy = [0,0,1,-1], [1,-1,0,0]
    matrix = [[0]*m for _ in range(n)]
    cnt = 0

    for i in range(k):
        bachu = list(map(int, sys.stdin.readline().split()))
        matrix[bachu[1]][bachu[0]] = 1

    for i in range(n):
        for j in range(m):
            if matrix[i][j]:
                cnt = bfs(i, j, cnt)

    print(cnt)