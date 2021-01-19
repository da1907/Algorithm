from sys import setrecursionlimit
setrecursionlimit(10**9)
import sys

def solve(x, y):
    print("x, y", x, y)
    print("visited", visited[x][y])
    if not visited[x][y]:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            print("nx ny", nx, ny)

            if 0 <= nx < N and 0 <= ny < N and board[x][y] < board[nx][ny]:
                visited[x][y] = max(visited[x][y], solve(nx, ny))
                print("!!!!!!", x, y)
        visited[x][y] += 1
        print("x, y, visited", x, y, visited[x][y])
    return visited[x][y]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
board = []

N = int(sys.stdin.readline())
visited = [[0] * N for _ in range(N)]

for i in range(N):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

maxV = 0
for i in range(N):
    for j in range(N):
        print("==========================")
        maxV = max(maxV, solve(i, j))

print(maxV)