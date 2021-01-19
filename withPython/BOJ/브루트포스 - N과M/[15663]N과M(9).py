import sys
N, M = map(int, sys.stdin.readline().split())
nums = []
nums = sorted(list(map(int, sys.stdin.readline().split())))
result, out = [], []
visited = [False] * N

def solve(depth):
    if depth == M:
        #result를 str 형태로 바꿔줌 왜냐면 바로 밑에줄을 해주려면 str 형태여야 비교 가능
        out_str = (' '.join(map(str, result)))
        if out_str not in out:
            out.append(out_str)
        return out

    for i in range(N):
        if visited[i]:
            continue
        result.append(nums[i])
        visited[i] = True
        solve(depth+1)
        result.pop()
        visited[i] = False

solve(0)
for i in out:
    print(i)