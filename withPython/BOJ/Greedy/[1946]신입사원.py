import sys
case = int(sys.stdin.readline())
rate = []

def solution(rate):
    rate = sorted(rate, key = lambda rate: rate[0])
    print(rate)




for _ in range(case):
    person = int(sys.stdin.readline())

    for _ in range(person):
        rate.append(list(map(int, sys.stdin.readline().split())))
        solution(rate)
print(rate)