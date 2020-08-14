import copy
import sys

def max_check(board):
    global maxV

    for i in range(N):
        for j in range(N):
            if board[i][j] > maxV :
                maxV = board[i][j]

def left(board):

    for i in range(N):
        value = 0
        idx = 0
        for j in range(N):
            if board[i][j] == 0:
                continue
            if value == 0:
                value = board[i][j]

            else:
                if board[i][j] == value:
                    board[i][idx] = value*2
                    board[i][j] = 0
                    value = 0
                    idx = idx + 1
                else:
                    board[i][idx] = value
                    value = board[i][j]
                    idx = idx + 1
            board[i][j] = 0

        if value != 0:
            board[i][idx] = value
    return board


def right(board):
    for i in range(N):
        value = 0
        idx = N-1
        for j in range(N-1, -1, -1):
            if board[i][j] == 0: continue
            if value == 0:
                value = board[i][j]
            else:
                if board[i][j] == value:
                    board[i][idx] = value*2
                    board[i][j] = 0
                    value = 0
                    idx = idx - 1
                else:
                    board[i][idx] = value
                    value = board[i][j]
                    idx = idx -1
            board[i][j] = 0

        if value != 0:
            board[i][idx] = value
    return board

def down(board):
    for i in range(N):
        value = 0
        idx = N-1
        for j in range(N-1, -1, -1):
            if board[j][i] == 0 : continue
            if value == 0:
                value = board[j][i]
            else:
                if board[j][i] == value:
                    board[idx][i] = value*2
                    board[j][i] = 0
                    idx = idx - 1
                    value = 0
                else:
                    board[idx][i] = value
                    value = board[j][i]
                    idx = idx - 1
            board[j][i] = 0
        if value != 0:
            board[idx][i] = value
    return board

def up(board):
    for i in range(N):
        value = 0
        idx = 0
        for j in range(N):
            if board[j][i] == 0: continue
            if value == 0:
                value = board[j][i]
            else:
                if value == board[j][i]:
                    board[idx][i] = value * 2
                    board[j][i] = 0
                    idx = idx + 1
                    value = 0
                else:
                    board[idx][i] = value
                    idx = idx + 1
                    value = board[j][i]
            board[j][i] = 0
        if value != 0:
            board[idx][i] = value
    return board


def dfs(board, cnt):
    if cnt == 5:
        max_check(board)
        return

    dfs(left(copy.deepcopy(board)), cnt + 1)
    dfs(right(copy.deepcopy(board)), cnt + 1)
    dfs(down(copy.deepcopy(board)), cnt + 1)
    dfs(up(copy.deepcopy(board)), cnt + 1)

maxV = 0

N = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

dfs(board, 0)
print(maxV)



