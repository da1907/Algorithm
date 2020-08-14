def solution(skill, skill_trees):
    cnt = 0
    stack = []

    for i in skill_trees:
        for k in range(len(skill) - 1, -1, -1):
            stack.append(skill[k])
        for j in range(len(i)):
            if i[j] in stack and stack[-1] != i[j]:
                break
            elif i[j] in stack and stack[-1] == i[j]:
                stack.pop()
        else:
            cnt += 1
    return cnt



skill = input()
skill_trees = list(input().split())
print(solution(skill, skill_trees))