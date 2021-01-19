import sys
sys.setrecursionlimit(100000)

def dfs(x, cnt):
    global result
    visited[x] = True
    if cnt == 5:        # cnt 5이면 결과 찾아낸것
        result = 1

    for i in friend[x]:         # 인접 노드 조사
        if not visited[i]:
            dfs(i, cnt+1)       # cnt 1 증가시켜준 상태로 재귀호출
            visited[i] = False      # 다음 조사를 위해 false로 바꿔주기
            if result:      # 결과 찾아냈으면 함수 종료
                return

N, M = map(int, input().split())
friend = [[] for _ in range(N+1)]
visited = [False] * N
result = 0

for _ in range(M):
    x, y = map(int, sys.stdin.readline().split())
    friend[x].append(y)     # 인접 노드 저장
    friend[y].append(x)

for i in range(N):
    if not visited[i]:      # 방문하지 않은 노드만 조사
        dfs(i, 1)
        visited[i] = False      # 한번 조사 끝난 노드는 다음 조사를 위해 False로 바꿔주기
        if result:      # 결과 나왔으면 더이상 조사하지 않고 반복문 종료
            break

print(result)
