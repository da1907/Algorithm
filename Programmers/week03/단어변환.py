def solution(begin, target, words):
    stack = [begin]
    visited = []
    maxV, time = 0, -1

    while stack:
        word = stack.pop()
        time += 1
        if word == target:
            maxV = max(maxV, time)
            time = 0
        visited.append(word)
        for i in words:
            if i not in visited:

                cnt = 0
                for j in range(len(i)):
                    if i[j] == word[j]:
                        continue
                    else:
                        cnt += 1
                if cnt == 1:
                    stack.append(i)
    return maxV

begin = input()
target = input()
words = list(input().split())

print(solution(begin, target, words))