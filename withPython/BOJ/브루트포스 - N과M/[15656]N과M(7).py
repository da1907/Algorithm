N, M = map(int, input().split())
nums = []
nums = sorted(list(map(int, input().split())))
result = []

def solve(depth):
    if depth == M:
        print(*result)
        return

    for i in range(N):
        result.append(nums[i])
        solve(depth+1)
        result.pop()

solve(0)