import sys
from copy import deepcopy
import itertools

n,m=map(int,input().split())
matrix=[list(map(int,[p for p in sys.stdin.readline().split()])) for _ in range(n)]
dx=[1,0,-1,0]
dy=[0,-1,0,1]
empty_wall=[]
virus=[]
maxV = 0

for i in range(n):
    for j in range(m):
        #벽을 둘수있는 좌표
        if matrix[i][j]==0:
            empty_wall.append([i,j])
        #바이러스 좌표
        if matrix[i][j]==2:
            virus.append([i,j])

def count_zero(maps):
    cnt=0
    for i in range(len(maps)):
        for j in range(len(maps[0])):
            if maps[i][j]==0:
                cnt+=1
    return cnt

def dfs(x,y,maps):
    for i in range(4):
        nx,ny=x+dx[i],y+dy[i]
        if nx<0 or nx>=n or ny<0 or ny>=m:
            continue
        if maps[nx][ny]==0:

            maps[nx][ny]=2
            dfs(nx,ny,maps)
    return maps

def solve(tmp):
    count = 0
    for x,y in virus:
        tmp=dfs(x,y,tmp)
        #print(ans)
    count = count_zero(tmp)
    return count

candidate=list(itertools.combinations(empty_wall,3))
for eq in candidate:
    tmp = deepcopy(matrix)
    for i,j in eq:
        tmp[i][j]=1
    vv=solve(tmp)
    maxV = max(maxV, vv)
print(maxV)