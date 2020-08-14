import sys
N, M = map(int, sys.stdin.readline().split())
nums = []
nums = sorted(list(map(int, sys.stdin.readline().split())))
visited = [False] * N
result, out = [], []

def solve(depth):
    if depth == M:
        print(' '.join(map(str, result)))
        return

    overlap = 0
    for i in range(N):
        if overlap != nums[i]:
            result.append(nums[i])
            overlap = nums[i]
            solve(depth+1)
            result.pop()

solve(0)