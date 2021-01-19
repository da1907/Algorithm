import sys
from collections import deque

dx = [-2, -2, -1, -1, 2, 2, 1, 1]       # 나이트가 움직일 수 있는 위치
dy = [-1, 1, -2, 2, -1, 1, -2, 2]

def solve(curX, curY, goalX, goalY):
    q = deque()
    q.append([curX, curY])
    a[curX][curY] = 1
    while q:
        curX, curY = q.popleft()

        # 현재 위치와 목표 위치가 같으면 함수 종료
        if curX == goalX and curY == goalY:
            return a[curX][curY] - 1

        # 8방향에 대해 반복
        for i in range(8):
            nx = curX + dx[i]
            ny = curY + dy[i]
            # 다음 위치가 범위내에 있고, 방문한 적이 없으면
            if 0 <= nx < l and 0 <= ny < l and a[nx][ny] == 0:
                q.append([nx, ny])      # 큐에 추가해주고
                a[nx][ny] = a[curX][curY] + 1       # 방문 횟수를 1 증가시켜 저장해준다


case = int(input())

for i in range(case):
    l = int(sys.stdin.readline())        # 체스판의 크기
    a = [[0] * l for _ in range(l)]
    curX, curY = map(int, sys.stdin.readline().split())     # 현재 위치
    goalX, goalY = map(int, sys.stdin.readline().split())   # 이동하려고 하는 위치
    print(solve(curX, curY, goalX, goalY))