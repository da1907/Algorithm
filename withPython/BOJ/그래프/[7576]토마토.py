import sys
from collections import deque
M, N = map(int, input().split())
box = []
tomatoes = deque()
day = -1
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for i in range(N):
    box.append(list(map(int, sys.stdin.readline().strip().split())))

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:
            tomatoes.append((i,j))

def solve():
    global day
    while tomatoes:
        day += 1
        size = len(tomatoes)
        for i in range(size):
            startx, starty = tomatoes.popleft()

            for i in range(4):
                tmp_x = startx + dx[i]
                tmp_y = starty + dy[i]

                if tmp_x < 0 or tmp_x >= N or tmp_y < 0 or tmp_y >= M:
                    continue
                if box[tmp_x][tmp_y] == 0:
                    box[tmp_x][tmp_y] = 1
                    tomatoes.append((tmp_x, tmp_y))
        #day += 1
        for i in box:
            print(i)
        print()
    return day

def check():
    global day
    for i in range(N):
        for j in range(M):
            if box[i][j]==0:
                day=-1
                return

solve()
check()
print(day)


#             rippen += 1
#         elif box[i][j] == 0:
#             unrippen += 1
#         elif box[i][j] == -1:
#             notomato += 1
# if rippen == N*M or rippen + notomato == N*M:
#     print(0)

