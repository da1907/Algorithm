import sys

case = int(sys.stdin.readline())

time = [[0]*2 for _ in range(case)]

for i in range(case):
    start, end = map(int, sys.stdin.readline().split())
    time[i][0] = start
    time[i][1] = end

time.sort(key = lambda x : (x[1], x[0]))

cnt = 1
end_time = time[0][1]
for i in range(1, case):
    if time[i][0] >= end_time:
        cnt += 1
        end_time = time[i][1]

print(cnt)