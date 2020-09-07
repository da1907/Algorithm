import sys
from itertools import combinations
from copy import deepcopy

def solution():


n, m = map(int, sys.stdin.readline().split())
board, cand = [], []
dx, dy = [0,0,1,-1], [1,-1,0,0]

for i in range(n):
    board.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(n):
    for j in range(m):
        if board[i][j] == 0:
            cand.append((i, j))

comb = combinations(cand, 3)
tmp = deepcopy(board)

for i in comb:
    for x, y in i:
        tmp[x][y] = 1
        solution(tmp)
        print(x, y)
