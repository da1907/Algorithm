N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
visited = [False] * N
result = []

def solve(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    overlap = 0
    for i in range(N):
        if visited[i] == False and overlap != nums[i]:
            result.append(nums[i])
            overlap = nums[i]
            solve(depth + 1)
            result.pop()
            visited[i] = True

            for j in range(i+1, N):
                visited[j] = False

solve(0)
