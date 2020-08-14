N, M = map(int, input().split())
num_list = [i+1 for i in range(N)]
out = []
visited = [False] * N

def solve(depth):
    #오름차순 정렬해 같지 않은것만 리스트에 넣기
    if depth == M:
        print(*out)
        return

    #중복 가능한 수열
    for i in range(N):
        if visited[i]:
            continue

        out.append(num_list[i])
        solve(depth+1)
        visited[i] = True
        out.pop()

        for j in range(i+1, N):
            visited[j] = False

solve(0)