import sys

def solution(li):
    stack = []
    check = True
    for i in range(len(li)):
        if li[i] == '(':
            stack.append(li[i])
        else:
            if not len(stack):
                return False
            else:
                stack.pop()
    if len(stack):
        return False
    else:
        return True


num = int(input())
result = []
for i in range(num):
    li = list(sys.stdin.readline().strip())
    if solution(li):
        result.append("YES")
    else:
        result.append("NO")

for i in result:
    print(i)