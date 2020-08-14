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
        if visited[i]:
            continue

        result.append(nums[i])
        solve(depth+1)
        result.pop()
        visited[i] = True

        for j in range(i+1, N):
            visited[j] = False

solve(0)
