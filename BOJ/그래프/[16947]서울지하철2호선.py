import sys
from collections import deque
sys.setrecursionlimit(100000)

N = int(input())
MAX = 3000
cycle = False
link = [[] for _ in range(MAX)]
visited = [False] * MAX
isCycle = [False] * MAX
check = [-1] * N

# 순환선인지 판단하기 위한 함수
def dfs(cur, start, cnt):
    global cycle
    if cur == start and cnt >= 2:      # 현재역이 시작역과 같고 두점 이상 지나왔으면
        cycle = True        # 순환역이 맞다
        return

    # 아닐 때 실행
    visited[cur] = True     # 방문한 역 표시
    for n in link[cur]:         # 다음 방문할 역 선택 -> 연결되어 있는 역
        if not visited[n]:      # 다음 방문할 역이 False 일때만 방문해야 하므로
            dfs(n, start, cnt + 1)      # 다음 방문할 역과 start, cnt 1증가된 값을 재귀호출
        # 다음 방문할 역이 이미 방문된 곳이면
        elif n == start and cnt >= 2:   # 다음 역과 시작 역이 같고 방문했던 역이 2곳 이상일 때
            dfs(n, start, cnt)          # cnt를 증가시키지 않은 상태로 재귀호출

# 각 역마다 순환역과 얼마나 떨어져 있는지 보는 함수
def bfs():
    global check        # 각 역의 순환역까지의 거리 저장 리스트
    q = deque()         # popleft 함수를 사용하기 위해 deque로 선언

    for i in range(N):
        if isCycle[i]:      # 순환역에 속하는 역이면
            check[i] = 0    # 거리는 0
            q.append(i)

    while len(q) != 0:  # q가 비면 종료
        cur = q.popleft()       # q에 저장되어있는 맨 첫 값을 pop

        for n in link[cur]:     # 현재 역과 연결되어 있는 역 중 다음 역 선택
            if check[n] == -1:  # 한번도 방문한적 없는 역일때만 실행
                q.append(n)
                check[n] = check[cur] + 1   # 현재 역까지의 거리 +1

    for i in check:
        print(i, end=' ')
    return

# 데이터 입력받기
for i in range(N):
    data = list(map(int, sys.stdin.readline().split()))
    link[data[0] - 1].append(data[1] - 1)
    link[data[1] - 1].append(data[0] - 1)

# 모든 역에 대해
for i in range(N):
    visited = [False] * N
    cycle = False
    dfs(i, i, 0)

    if cycle:   #cycle이 True로 바뀌어 반환됐으면
        isCycle[i] = True       #순환역이라고 표시

bfs()