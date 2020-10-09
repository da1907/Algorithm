# 테스트10에서만 시간초과
# def solution(number, k):
#     numbers = list(map(int, list(number)))
#     idx = 0
#     answer = ''
#
#     for i in range(len(numbers)-k):
#         maxV = 0
#         print("-----")
#         for j in range(idx, k+1):
#             if maxV < numbers[j]:
#                 maxV = numbers[j]
#                 print("m", maxV)
#         print("1>",idx,k,answer)
#         idx += numbers[0+idx:k+1].index(maxV) + 1
#         k += 1
#         answer += str(maxV)
#         print("2>",idx, k, answer)
#
#     return answer

def solution(number, k):
    stack = []
    for i in number:
        while stack and i > stack[-1]:
                if k > 0:
                    stack.pop()
                    k -= 1
                else:
                    break
        stack.append(i)

    if k > 0:
        for i in range(k):
            stack.pop()

    answer = "".join(stack)
    return answer



print(solution("54321", 2))