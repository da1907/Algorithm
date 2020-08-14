N, M = map(int, input().split())
nums = []
result = []
visited = [False] * N
nums = sorted(list(map(int, input().split())))

def solve(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        if visited[i]:      #visited가 True면 그냥 넘어가기
            continue
        result.append(nums[i])
        visited[i] = True
        solve(depth+1)
        result.pop()

        #i는 True로 유지되어야 (7,1) 같은 형태가 안나오므로 i 뒤부터 False로 바꿔주기
        for j in range(i+1, N):
            visited[j] = False

solve(0)