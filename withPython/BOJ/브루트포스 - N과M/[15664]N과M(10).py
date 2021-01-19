import sys
N, M = map(int, sys.stdin.readline().split())
nums = []
nums = sorted(list(map(int, sys.stdin.readline().split())))
result, out = [], []
visited = [False] * N

def solve(depth):
    if depth == M:
        out_str = (' '.join(map(str, result)))
        if out_str not in out:
            out.append(out_str)
        return out

    for i in range(N):
        if visited[i] == False:
            result.append(nums[i])
            visited[i] = True
            solve(depth+1)
            result.pop()

            for j in range(i+1, N):
                visited[j] = False

solve(0)
for i in out:
    print(i)

