import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())

visited = [0] * 100001
queue = []
queue = deque()
cnt = -1

queue.append(n)
while queue:
    cnt += 1
    for i in range(len(queue)):
        x = queue.popleft()
        visited[x] = 1
        if x == k:
            print(cnt)
            exit()
        if 0 <= x-1 and not visited[x-1]:
            queue.append(x-1)
        if x+1 <100001 and not visited[x+1]:
            queue.append(x+1)
        if 2*x < 100001 and not visited[2*x]:
            queue.append(2*x)