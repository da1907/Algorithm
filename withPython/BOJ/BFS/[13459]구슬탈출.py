import sys
from collections import deque
input = sys.stdin.readline

def solution():
    cnt = 0
    rqueue = deque()
    bqueue = deque()
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for i in range(n):
        for j in range(m):
            if board[i][j] == 'R':
                rqueue.append((i, j))
            if board[i][j] == 'B':
                bqueue.append((i, j))

    while rqueue:
        rx, ry = rqueue.popleft()
        print("r",rx, ry)
        visited[rx][ry] = 1
        bx, by = bqueue.popleft()
        print("b",bx, by)

        for i in range(4):
            rnx, rny = rx+dx[i], ry+dy[i]
            bnx, bny = bx+dx[i], by+dy[i]
            if 0 <= rnx < n and 0 <= rny < m and not visited[rnx][rny] and board[rnx][rny] != '#':
                visited[rnx][rny] = 1
                while True:
                    if board[rnx][rny] == '#':
                        rqueue.append((rnx-dx[i], rny-dy[i]))
                        cnt += 1
                        bqueue.append((bnx-dx[i], bny-dy[i]))
                        break
                    elif board[rnx][rny] == 'O':
                        if 0<=bnx+dx[i]<n and 0<=bny+dy[i]<m and board[bnx+dx[i]][bny+dy[i]] == 'O':
                            cnt += 11
                        return cnt
                    elif board[rnx][rny] == 'B':
                        if board[rnx+dx[i]][rny+dy[i]] == '.':
                            rnx, rny = bnx, bny
                            bnx, bny = rnx+dx[i], rny+dy[i]
                            print("b", bnx, bny)
                            print("r", rnx, rny)
                        else:
                            break
                    else:
                        rnx, rny = rnx+dx[i], rny+dy[i]
                        visited[rnx][rny] = 1
                        if 0<=bnx+dx[i]<n and 0<=bny+dy[i]<m and (board[bnx+dx[i]][bny+dy[i]] == '.' or board[bnx+dx[i]][bny+dy[i]] == 'R'):
                            bnx, bny = bnx+dx[i], bny+dy[i]
                print(rnx, rny, "///", bnx, bny)
    return cnt
dx, dy = [0,0,-1,1], [-1,1,0,0]

board = []
n, m = map(int, input().split())

for i in range(n):
    board.append(list(input().strip()))

if 0 < solution() <= 10:
    print(1)
else:
    print(0)