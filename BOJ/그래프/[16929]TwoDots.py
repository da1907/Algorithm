import sys

dx = [-1, 1, 0, 0]      # 이동가능 방향
dy = [0, 0, -1, 1]
cycle = False

def dfs(x, y, curX, curY, cnt, color):
    global cycle
    if cycle:      # 사이클을 하나라도 찾았으면 더이상 안찾아도 되므로 함수 종료
        return

    visited[curX][curY] = True      # 방문 표시
    # 현재 위치가 시작점으로 돌아왔고, 4개의 점 이상 지나왔으면
    if x == curX and y == curY and cnt >= 4:
        cycle = True        # 사이클이다
        return         # 함수 종료

    for i in range(4):      # 가능한 네 방향 조사
        nx = curX + dx[i]
        ny = curY + dy[i]

        if 0 <= nx < N and 0 <= ny < M:     # 다음 위치가 범위 내에 있고
            # 방문한 적이 없으며 색이 같으면
            if not visited[nx][ny] and color == board[nx][ny]:
                dfs(x, y, nx, ny, cnt+1, color)     # cnt 1 증가 후 깊이우선탐색
            # 방문한 적이 있으면 시작점으로 다시 돌아온 것인지 검사
            elif nx == x and ny == y and cnt >= 4:
                dfs(x, y, nx, ny, cnt, color)   # 맞으면 cnt 증가 시키지 않고 재귀호출
    return      # 사이클 찾지 못했을 경우 종료


N, M = map(int, input().split())
board = []

for i in range(N):      # 게임판 받아오기
    board.append(list(sys.stdin.readline().strip()))

for i in range(N):
    for j in range(M):      # 게임판의 모든 부분 탐색
        # 새로 시작할 때마다 visited 모두 False로 초기화
        visited = [[False] * M for _ in range(N)]
        visited[i][j] = True
        dfs(i, j, i, j, 1, board[i][j])

if cycle:
    print("Yes")
else:
    print("No")