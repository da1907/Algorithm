import sys
case = int(sys.stdin.readline())
rope = []

for _ in range(case):
    rope.append(int(sys.stdin.readline().strip()))

rope.sort()

maxx = 0
for i in range(case):
    weight = 0
    weight += rope[i] * (len(rope) - i)

    maxx = max(maxx, weight)

print(maxx)