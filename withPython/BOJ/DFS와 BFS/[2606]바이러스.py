import sys

computer = int(input())
link = int(input())
matrix = [[0] * (computer+1) for _ in range(computer+1)]
node = []

for _ in range(link):
    node = list(map(int, sys.stdin.readline().split()))
    matrix[node[0]][node[1]] = 1
    matrix[node[1]][node[0]] = 1

