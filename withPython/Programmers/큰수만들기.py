# 테스트10에서만 시간초

# def solution(number, k):
#     numbers = list(map(int, list(number)))
#     idx = 0
#     answer = ''
#
#     for i in range(len(numbers)-k):
#         maxV = 0
#
#         for j in range(idx, k+1):
#             if maxV < numbers[j]:
#                 maxV = numbers[j]
#
#         idx += numbers[0+idx:k+1].index(maxV) + 1
#         k += 1
#         answer += str(maxV)
#
#     return answer

def solution(number, k):
    # 1
    stack = []
    # 2
    for i in number:
        # 3
        while stack and i > stack[-1]:
            # 4
            if k > 0:
                stack.pop()
                k -= 1
            # 5
            else:
                break
        # 3-1
        stack.append(i)

    # 6
    if k > 0:
        for i in range(k):
            stack.pop()

    # 7
    answer = "".join(stack)
    return answer

print(solution("54321", 2))