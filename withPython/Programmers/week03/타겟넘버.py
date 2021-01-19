def solution(numbers, target):
    # 1
    n = len(numbers)
    answer = 0

    # 2
    def dfs(idx, total):

        # 3
        if idx == n:
            if total == target:
                nonlocal answer
                answer += 1

        # 4
        else:
            dfs(idx+1, total+numbers[idx])
            dfs(idx+1, total-numbers[idx])

    # 1-2
    dfs(0, 0)
    return answer


numbers = list(map(int, input().split()))
target = int(input())

print(solution(numbers, target))