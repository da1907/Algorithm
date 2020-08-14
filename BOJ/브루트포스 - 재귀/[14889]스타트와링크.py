import sys
import itertools

N = int(input())
arr = []
member = [i for i in range(N)]

for i in range(N):
    arr.append(list(map(int, sys.stdin.readline().strip().split())))

def team(member):
    allMember = [i for i in range(N)]
    start = []
    link = []

    for i in allMember:
        if i in member:
            start.append(i)
        else:
            link.append(i)

    startSum = 0
    for i in start:
        for j in start:
            startSum += arr[i][j]

    linkSum = 0
    for i in link:
        for j in link:
            linkSum += arr[i][j]

    return abs(startSum - linkSum)

def solve(member):
    combination_members = itertools.combinations(member, int(N/2))
    selected_members = list(combination_members)
    length = int(len(selected_members)/2)

    minVal = sys.maxsize
    for member in selected_members[:length]:
        minus = team(member)

        if minVal > minus:
            minVal = minus

    print(minVal)

solve(member)