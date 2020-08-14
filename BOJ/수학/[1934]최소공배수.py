import sys
import math     #math.gcd 사용하기 위한 방법
case = int(input())

#직접 gcd 구해서 하는 방법
# def gcd(a, b):
#     mod = 1
#     while mod > 0:
#         mod = a % b
#         a = b
#         b = mod
#         mod = a % b
#     return b

for i in range(case):
    a, b = map(int, sys.stdin.readline().strip().split())

    if b % a == 0:
        print(max(a,b))
    else:
        print(a * b // math.gcd(a, b))