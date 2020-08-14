#depth = 0 으로 초기화
N, M = map(int, input().split())
visited = [False] * N
out = []

def solve(depth, N, M):
    if depth == M:
        print(' '.join(map(str, out)))  #list를 str 타입으로 합쳐 출력
        return

    for i in range(len(visited)):   #탐사 체크 하면서
        if not visited[i]:  #탐사 안했다면
            visited[i] = True   #탐사 시작하면서 true로 바꿔서 중복방지
            out.append(i+1)     #i는 0부터 시작하므로 +1 해준 값 추가
            solve(depth+1, N, M)    #깊이 우선 탐색
            visited[i] = False  #깊이 탐사 완료
            out.pop()   #탐사한 내용 제거

solve(0, N, M)
