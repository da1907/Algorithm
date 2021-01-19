import sys
s = 0

N = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr)

for i in range(N):
    if s+1 >= arr[i]:
        s = s + arr[i]

print(s + 1)