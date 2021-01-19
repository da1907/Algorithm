def solution(s):
    for i in s:
        if i == '(':
            stack.append(i)
        else:
            if len(stack):
                stack.pop()
            else:
                return False
    if not len(stack):
        return True
    else:
        return False

stack = []
s = list(input())
print(solution(s))
