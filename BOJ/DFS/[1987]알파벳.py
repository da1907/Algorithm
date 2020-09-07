import sys
input = sys.stdin.readline

# def solution(r, c, board):
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#     visited = [0] * 26
#     answer, maxV= 0, 1
#     visited[ord(board[0][0]) - 65] = 1
#
#     def dfs(x, y, cnt):
#         nonlocal maxV
#         visited[ord(board[x][y]) - 65] = 1
#         for i in range(4):
#             nx, ny = x + dx[i], y + dy[i]
#             if 0 <= nx < r and 0 <= ny < c and not visited[ord(board[nx][ny]) - 65]:
#                 visited[ord(board[nx][ny]) - 65] = 1
#                 dfs(nx, ny, cnt+1)
#                 visited[ord(board[nx][ny]) - 65] = 0
#         maxV = max(cnt, maxV)
#     dfs(0, 0, 1)
#     return maxV

def bfs():
    # 1
    maxV = 0
    queue = set()
    queue.add((0, 0, board[0][0]))

    # 2
    while queue:

        # 3
        x, y, visited = queue.pop()
        maxV = max(maxV, len(visited))

        # 4
        if maxV == 26:
            return 26

        # 5
        for i in range(4):
            nx, ny = x+dx[i], y+dy[i]

            # 6
            if 0<=nx<r and 0<=ny<c and board[nx][ny] not in visited:
                queue.add((nx, ny, visited + board[nx][ny]))
    return maxV

r, c = map(int, input().split())
board = []
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

for i in range(r):
    board.append(list(input().strip()))
print(bfs())