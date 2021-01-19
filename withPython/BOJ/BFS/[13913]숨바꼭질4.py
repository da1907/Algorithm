from collections import deque

def bfs(q, N, K):
    global cnt
    while q:        #q가 다 비워지면 종료
        for _ in range(len(q)):
            find = q.popleft()
            if find == K:       #find가 K와 같아지면 함수 종료
                p = []
                while find != N:        #경로 찾기위한 반복문
                    p.append(find)
                    find = path[find]

                # 위 반복문 조건이 N과 같으면 종료해야하므로 N은 따로 추가
                p.append(N)
                p.reverse()     #뒤집어주기
                print(cnt)
                print(' '.join(map(str, p)))
                return

            for nx in (find-1, find+1, find*2):
                if 0 <= nx < 100001 and not visited[nx]:
                    visited[nx] = True
                    path[nx] = find
                    q.append(nx)

        cnt += 1

N, K = map(int, input().split())
visited = [False] * 100001
q = deque([N])
cnt = 0
path = [0] * 100001
bfs(q, N, K)
