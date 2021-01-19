import sys
input = sys.stdin.readline
MAX = 30
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
visited = [[False] * MAX for _ in range(MAX)]
result = []         # 각 단지별 집의 갯수 저장하기 위한 리스트

def dfs(x, y):
    global cnt
    if not visited[x][y]:           # 방문한적 없을 때만 실행
        visited[x][y] = True        # 방문 표시
        cnt += 1                    # 집 갯수 1 증가
        for i in range(4):          # 상하좌우 조사
            nx = x + dx[i]
            ny = y + dy[i]

            # 다음 조사할 부분이 범위내에 있고, 집이면
            if 0 <= nx <= N-1 and 0 <= ny <= N-1 and apart[nx][ny]:
                apart[nx][ny] = cnt     # 그 위치에 단지번호 저장시켜주기
                dfs(nx, ny)             # 재귀함수 호출


N = int(input())
apart = [list(map(int, list(input().strip()))) for _ in range(N)]

for i in range(N):
    for j in range(N):      # 표의 모든 부분 조사
        if apart[i][j] and not visited[i][j]:   # 집이 있고, 방문한적 없으면 실행
            cnt = 0         # cnt 0 초기화
            dfs(i, j)
            result.append(cnt)      # 해당 단지내 집의 갯수를 결과 리스트에 저장

result.sort()           # 정렬

print(len(result))      #몇단지까지 있는가 출력
for i in result:        #각 단지별 집의 수 출력
    print(i)