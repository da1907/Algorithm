from collections import deque

def bfs(q, K):
    global cnt
    while q:        #q가 다 비워질때까지
        for i in range(len(q)):         #q의 길이만큼 반복
            find = q.popleft()          #제일 첫 값 pop 해주기
            if not visited[find]:       #방문한 적 없을때만 실행
                visited[find] = True
                if find == K:           #find와 목표값 같으면 cnt 반환
                    return cnt

                if find - 1 >= 0:       #범위 벗어나지 않는지 체크
                    q.append(find-1)
                if find + 1 < 100001:
                    q.append(find+1)
                if find * 2 < 100001:
                    q.append(find*2)
        print(q)
        cnt += 1        #q내의 모든 요소 다 비교하면 cnt 1 증가

N, K = map(int, input().split())
visited = [False] * 100001
q = deque([N])
cnt = 0

print(bfs(q, K))
