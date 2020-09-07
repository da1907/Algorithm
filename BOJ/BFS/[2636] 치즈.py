import sys
from collections import deque
input = sys.stdin.readline

def check(board, queue):
    visited = [[0 for _ in range(n)]] * m
    while queue:
        node = queue.popleft()
        x = node[0]
        y = node[1]

        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < m and 0 <= ny < n and not board[nx][ny]:
                board[nx][ny] = -1
                visited[nx][ny] = 1
                queue.append([nx, ny])
    return board

def melt(change, board):
    global cnt
    cnt += 1
    while change:
        a, b = change.pop()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if not board[na][nb] and [na, nb] not in hole:
                hole.append([na, nb])
        board[a][b] = -1
    check(board, hole)
    return board

def solution(board):
    count = 0
    queue = deque([[0, 0]])
    board = check(board, queue)

    for x in range(m):
        for y in range(n):
            if board[x][y] == 1:
                count += 1
    cheese.append(count)

    while True:
        chk = False
        count = 0
        for x in range(m):
            for y in range(n):
                if board[x][y] == 1:
                    for i in range(4):
                        nx, ny = x + dx[i], y + dy[i]
                        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == -1:
                            change.append((x, y))
                            break

        board = melt(change, board)

        for x in range(m):
            for y in range(n):
                if board[x][y] == 1:
                    chk = True
                    count += 1
        cheese.append(count)
        if not chk:
            return (cnt, cheese[-2])

m, n = map(int, input().split())
dx, dy = [1, -1, 0, 0], [0, 0, 1, -1]
board = []
change = []
cheese = []
cnt = 0
chk = False
hole = deque()
for i in range(m):
    board.append(list(map(int, input().strip().split())))

for i in solution(board):
    print(i)
#print(*solution(board))