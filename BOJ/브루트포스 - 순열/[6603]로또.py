import sys
from itertools import combinations  #조합 함수 사용
arr = []

while True:
    arr = list(map(int, sys.stdin.readline().strip().split()))

    if arr[0] == 0:     #0 받으면 종료
        break

    for i in combinations(arr[1:], 6):
        print(' '.join(map(str, i)))
    print()