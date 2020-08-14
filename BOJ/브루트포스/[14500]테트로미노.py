import sys
N, M = map(int, input().split())
graph = []

for _ in range(N):
    graph.append(list(map(int, sys.stdin.readline().strip().split())))

#블록의 뒤집기나 돌리기를 해서 나올수 있는 모든 경우의 수((0,0)을 기준으로 함)
block = [
    [(0, 1), (1, 0), (1, 1)],  # ㅁ 모양
    [(0, 1), (0, 2), (0, 3)],
    [(1, 0), (2, 0), (3, 0)],
    [(0, 1), (0, 2), (1, 0)],  # ㄱ 모양
    [(0, 1), (0, 2), (-1, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 2)],
    [(1, 0), (2, 0), (2, 1)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 1), (1, 0), (2, 0)],
    [(1, 0), (2, 0), (2, -1)],
    [(1, 0), (1, 1), (2, 1)],  # ㄹ 모양
    [(0, 1), (1, 0), (-1, 1)],
    [(0, 1), (1, 0), (1, -1)],
    [(0, 1), (1, 1), (1, 2)],
    [(0, 1), (0, 2), (1, 1)],  # ㅜ 모양
    [(1, -1), (1, 0), (1, 2)],
    [(1, 0), (2, 0), (1, -1)],
    [(1, 0), (1, 1), (2, 0)]
]

def tetromino(x,y):
    global ans
    for i in range(19):
        s = graph[x][y]
        for j in range(3):
            try:
                nx = x + block[i][j][0]
                ny = y + block[i][j][1]
                s += graph[nx][ny]
            except IndexError:
                continue
        ans = max(ans, s)

#판의 모든 지점을 비교
def solve():
    for i in range(N):
        for j in range(M):
            tetromino(i, j)

ans = 0
solve()
print(ans)