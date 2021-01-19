from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def bfs():
    result = 0
    while q:
        result += 1
        print("res",result)

        for _ in range(len(q)):
            x, y = q.popleft()
            print("x y", x,y)
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                print("nx ny", nx,ny)
                if 0 <= nx < n and 0 <= ny < m:
                    if a[nx][ny] == 0:
                        a[nx][ny] = 1
                        print(a)
                        q.append([nx, ny])
                        print(q)
    return result

m, n = map(int, input().split())
a, q = [], deque()
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        if row[j] == 1:
            q.append([i, j])
    a.append(row)

result = bfs() - 1
for i in range(n):
    for j in range(m):
        if a[i][j] == 0:
            print(-1)
            exit()
print(result)