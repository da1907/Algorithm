import sys
N = int(input())
mapp = []
gu1, gu2, gu3, gu4 = 0, 0, 0, 0

for i in range(N):
    mapp.append(list(map(int, sys.stdin.readline().split())))

##1번 구역 합 구하기
def sum_1D(graph, x, y, d1, d2):
    sum_1 = 0
    for i in range(0, x+d1):

for x in range(0,N-1):
    for y in range(0, N-1):
        for d1 in range(0, N-1-x):
            for d2 in range(0, N-1-y):
                mapp[]