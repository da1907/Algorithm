import sys

def solution(dirs):
    visited = [[0, 0, 0, 0] for _ in range(len(dirs))]
    cnt = 0
    x, y =0, 0
    for i in range(len(dirs)):
        if dirs[i] == 'U':
            d = [0, 1]
        elif dirs[i] == 'D':
            d = [0, -1]
        elif dirs[i] == 'L':
            d = [-1, 0]
        elif dirs[i] == 'R':
            d = [1, 0]
        nx, ny = x+d[0], y+d[1]
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            if [x, y, nx, ny] not in visited and [nx, ny, x, y] not in visited:
                visited.append([x, y, nx, ny])
                cnt += 1
                x, y = nx, ny
            else:
                x, y = nx, ny
    return cnt

dirs = list(sys.stdin.readline().strip())
print(solution(dirs))