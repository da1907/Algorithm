import sys
input = sys.stdin.readline

def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a%b)

def solution(w, h):
    if w < h:
        w, h = h, w
    g  = gcd(w, h)

    return w * h - (w + h - g)

w, h = map(int, input().split())
print(solution(w, h))