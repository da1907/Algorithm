def solution(n, words):
    arr = [words[0]]
    for i in range(1, len(words)):
        if words[i] not in arr and words[i-1][-1] == words[i][0]:
            arr.append(words[i])
            print(arr)
        else:
            # who = (i+1) % n when = (i+1) // n
            return [(i%n) +1, (i//n) +1]
    return [0, 0]

n = int(input())
words = list(input().split())
solution(n, words)


