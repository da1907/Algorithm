from collections import deque

def solution(n, computers):
    # 1
    answer = 0                          # 네트워크 갯수
    visited = [0 for i in range(n)]     # 방문 여부
    queue = deque()                     # 탐색해야 할 노드 저장하는 큐

    # 2
    while 0 in visited:                 # 모든 노드를 방문할 때 까지 실행
        node = visited.index(0)
        queue.append(node)              # 방문 하지 않은 노드부터 시작
        visited[node] = 1               # 방문 체크

        # 3
        while queue:                    # queue에 값 존재하면 수행

            # 3-1
            com = queue.popleft()       # 제일 첫 value 꺼내오기

            # 3-2
            for i in range(n):

                # 3-2-1
                if not visited[i] and computers[com][i] == 1:
                    queue.append(i)
                    visited[i] = 1
        answer += 1                     # 한 네트워크가 끝나면 네트워크 갯수 1 증가

    return answer


n = int(input())
computers = []
for i in range(n):
    computers.append(list(map(int, input().split())))

print(solution(n, computers))