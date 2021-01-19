import sys
from collections import deque

def dfs(start):
    visited = []
    stack = [start]

    while stack:
        tmp = []
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            for i in range(N):
                if matrix[node-1][i] == 1 and (i+1) not in visited:
                    tmp.append(i+1)
                    tmp = sorted(tmp, reverse = True)
            stack.extend(tmp)

    return visited

def bfs(start):
    visited = []
    queue = deque([start])

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.append(node)
            for i in range(N):
                if matrix[node-1][i] == 1 and (i+1) not in visited:
                    queue.append(i+1)
    return visited


line = []
N, M, V = map(int, sys.stdin.readline().split())
matrix = [[0] * N for _ in range(N)]

for i in range(M):
    line = list(map(int, sys.stdin.readline().split()))
    matrix[line[0]-1][line[1]-1] = 1
    matrix[line[1]-1][line[0]-1] = 1

# for i in range(M):
#     line.append(list(map(int, sys.stdin.readline().split())))
# print(line)

print(*dfs(V))
print(*bfs(V))