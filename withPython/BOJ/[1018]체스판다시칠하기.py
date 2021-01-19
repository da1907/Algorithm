import sys

N, M = map(int, input().split())
board = []
cnt = 0
ans = 999999

for i in range(N):
    board.append(list(sys.stdin.readline().strip()))

for i in range(N-7):
    for j in range(M-7):
        #WB
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] == 'B':
                        cnt += 1
                else:
                    if board[k][l] == 'W':
                        cnt += 1

        ans = min(cnt, ans)
        cnt = 0

        #BW
        for k in range(i, i+8):
            for l in range(j, j+8):
                if (k+l) % 2 == 0:
                    if board[k][l] == 'W':
                        cnt += 1
                else:
                    if board[k][l] == 'B':
                        cnt += 1
        ans = min(cnt, ans)
        cnt = 0

print(ans)

