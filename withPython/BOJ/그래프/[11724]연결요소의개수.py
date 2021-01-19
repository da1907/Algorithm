import sys
sys.setrecursionlimit(10000)
N, M = map(int, input().split())    #N, M 받아오기
link = [[] for i in range(N+1)]     #쿠션 값 주기위해 n+1만큼 리스트 만듬
cnt = 0
visited = [False] * (N + 1)

#dfs 탐색 하기위한 함수
def dfs(i):
    visited[i] = True       #visited[i] True로 바꾸고
    for j in link[i]:       #i 인덱스에 연결된 정점 수 만큼 반복
        if not visited[j]:  #연결된 정점 방문 안했으면
            dfs(j)          #연결된 정점 기준으로 dfs 재귀 탐색

#run시 제일 먼저 실행
for i in range(M):
    data = list(map(int, sys.stdin.readline().split()))  #데이터 한줄씩 받아옴
    link[data[0]].append(data[1])           #서로 연결되어있으므로 서로를 서로에게 저장시켜줌
    link[data[1]].append(data[0])

for i in range(1, N+1):     #정점은 1부터 시작하므로 1부터 반복
    if not visited[i]:      #해당 정점 방문한적 없으면
        cnt += 1            #cnt 1 증가시키고
        dfs(i)              #dfs 함수 실행

print(cnt)