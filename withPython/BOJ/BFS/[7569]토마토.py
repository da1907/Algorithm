import sys
from collections import deque

def solution(queue):
    global cnt

    while(queue):
        for i in range(len(queue)):
            z, y, x = queue.popleft()
            if matrix[z][y][x] == -1 or not matrix[z][y][x]:
                continue
            for i in range(6):
                nx = x + dx[i]
                ny = y + dy[i]
                nz = z + dz[i]

                if 0<=nx<m and 0<=ny<n and 0<=nz<h and not matrix[nz][ny][nx]:
                    matrix[nz][ny][nx] = cnt
                    queue.append((nz, ny, nx))
        cnt += 1
    return matrix

cnt = 1
queue = deque()
m, n, h = map(int, sys.stdin.readline().split())
matrix = [[[]* m for _ in range(n)] for _ in range(h)]
dx, dy, dz = [0, 0, -1, 1, 0, 0], [1, -1, 0, 0, 0, 0], [0, 0, 0, 0, -1, 1]
maxV = 0
flag = False

# 입력받기
for i in range(h):
    for j in range(n):
        matrix[i][j] = list(map(int, sys.stdin.readline().split()))

# matrix에 0 하나도 없으면 0일 출력해야하므로 check
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                flag = True
if not flag:
    print(0)
    exit()

# matrix에 1인부분 모두 queue에 저장
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 1:
                queue.append((i, j, k))
matrix = solution(queue)

# 모든 토마토를 익게 했는데 안익은 토마토(0) 여전히 있으면 -1 출력
for i in range(h):
    for j in range(n):
        for k in range(m):
            if matrix[i][j][k] == 0:
                print(-1)
                exit()

# 모든 토마토 익게한 후 제일 오래 걸린 일수 출력
for i in range(h):
    for j in range(n):
        for k in range(m):
            maxV = max(maxV, matrix[i][j][k])
print(maxV)

