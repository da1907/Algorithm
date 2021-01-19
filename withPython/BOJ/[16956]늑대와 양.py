import sys
input = sys.stdin.readline

def solution(board):
    for i in range(r):
        for j in range(c):
            if board[i][j] == 'S':
                continue
            elif board[i][j] == 'W':
                for k in range(4):
                    nx, ny = i + dx[k], j + dy[k]
                    if 0<=nx<r and 0<=ny<c and board[nx][ny] == 'S':
                        return 0
            else:
                board[i][j] = 'D'
    return 1

r, c = map(int, input().split())
board = []
dx, dy = [1, -1, 0, 0], [0, 0, -1, 1]

for i in range(r):
    board.append(list(input().strip()))

result = solution(board)
if solution(board):
    print(result)
    for i in range(r):
        for j in range(c):
            print(board[i][j], end='')
        print()
else:
    print(result)