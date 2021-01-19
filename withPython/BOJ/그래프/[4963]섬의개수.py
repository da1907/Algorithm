import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]

def dfs(x, y):
    for i in range(8):      # 8뱡향 모두 조사
        nx = x + dx[i]
        ny = y + dy[i]
        # 지도를 벗어나지 않으면서 육지이면
        if 0 <= nx <= h-1 and 0 <= ny <= w-1 and graph[nx][ny]:
            graph[nx][ny] = 0   #재방문 하지 않기위해 0으로 만들어 주기
            dfs(nx, ny)


while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:       # 0 0 입력받으면 종료
        break

    graph = [list(map(int, input().split())) for _ in range(h)]

    cnt = 0
    for i in range(h):
        for j in range(w):          # 지도 맨 처음부터 훑다가
            if graph[i][j]:         # 육지 나오면 시작
                cnt += 1
                dfs(i, j)

    print(cnt)