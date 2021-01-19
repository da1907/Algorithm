from collections import deque

max = 1000
S = int(input()) *2
dist = [[0]*S for _ in range(S)]

screen = 1
clipboard = 0
cnt = 0

def bfs():
    global cnt
    q = deque()
    q.append((1,0))
    while q:
        x, y = q.popleft()

        if x == S//2:
            return dist[x][y]

        for nx, ny in (x, x), (x+y, y), (x-1, y):
            if nx < 0 or nx > S:
                continue
            if not dist[nx][ny]:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y]+1
print(bfs())