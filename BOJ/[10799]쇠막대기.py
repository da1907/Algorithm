def solution(li):
    stack = []
    cnt = 0
    for i in range(len(li)):
        if li[i] == '(':
            stack.append(li[i])
        elif li[i] == ')' and li[i-1] == '(':
            stack.pop()
            cnt += len(stack)
        elif li[i] == ')' and li[i-1] == ')':
            stack.pop()
            cnt += 1
    return cnt

li = list(input())
print(solution(li))