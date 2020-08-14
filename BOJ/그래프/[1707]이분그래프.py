import sys
sys.setrecursionlimit(100000)

def dfs(now, color):
    visited[now] = color
    for i in link[now]:     # 인접한 노드들 중
        if not visited[i]:  # 방문한 적 없는 노드만 검사
            if not dfs(i, -color):  # color 교차한 상태로 재귀호출
                return False
        elif visited[i] == visited[now]:    # 이전노드와 다음노드가 같은 색이면 이분화 안된 것
            return False
    return True

case = int(input())
for _ in range(case):
    V, E = map(int, sys.stdin.readline().split())
    link = [[] for _ in range(V)]

    for _ in range(E):
        x, y = map(int, sys.stdin.readline().split())
        link[x-1].append(y-1)       # 인접 노드 저장
        link[y-1].append(x-1)
    visited = [0] * V
    ans = True

    for i in range(V):
        if not visited[i]:      # 방문한 적 없는 노드만 검사
            if not dfs(i, 1):
                ans = False
                break
    if ans:         # 모든 검사 끝나고 false 리턴하지 않으면 이분 그래프
        print("YES")
    else:
        print("NO")