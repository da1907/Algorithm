import sys
from collections import deque
dx = [-1, 1, 0, 0]      # 이동 가능한 위치
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append([x, y])
    visited[x][y] = True
    dist[x][y] = 1      # (1, 1)칸도 포함한다고 했으므로

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 다음 위치가 범위 내에 있으면서 방문한적 없고 1, 즉 이동 가능한 칸이면
            if 0 <= nx < N and 0 <= ny < M and not visited[nx][ny]:
                if maze[nx][ny] == 1:
                    q.append([nx, ny])      # 탐색해야할 후보 목록에 넣어놓는다
                    dist[nx][ny] = dist[x][y] + 1       # 거리 리스트에 현재거리 +1 을 저장
                    visited[nx][ny] = True      # 방문 표시
    return dist[N-1][M-1]

N, M = map(int, input().split())
maze = []
visited = [[False] * M for _ in range(N)]
dist = [[0] * M for _ in range(N)]

for i in range(N):
    maze.append(list(map(int, sys.stdin.readline().strip())))

print(bfs(0, 0))