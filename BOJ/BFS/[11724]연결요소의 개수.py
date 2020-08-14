import sys

def dfs(x, y):
    print("!!!",stack)


n, m = map(int, sys.stdin.readline().split())
link = [[0]*n for _ in range(n)]
stack = []
for i in range(m):
    temp = list(map(int, sys.stdin.readline().split()))
    print(temp)
    link[temp[0]-1][temp[1]-1] = 1
    link[temp[1]-1][temp[0]-1] = 1

for i in range(m):
    for j in range(m):
        if link[i][j] == 1:
            stack = [i, j]
            dfs(i, j)
print(link)