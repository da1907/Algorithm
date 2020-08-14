import sys
import itertools

n = int(sys.stdin.readline())
op = [c for c in sys.stdin.readline().split()]

minn = []
maxx = []
num = [i for i in range(10)]
flag = [False] * 10
permu = itertools.permutations(num, n+1)

for i in permu:
    for j in range(i):
        if op[]
    print(i)
#print(list(permu))
#def solve():
