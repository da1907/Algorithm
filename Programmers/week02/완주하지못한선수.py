# def solution(participant, completion):
#     for i in participant:
#         if i not in completion:
#             return i
#         else:
#             completion.remove(i)
#
#print(solution(participant, completion))

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]


participant = list(input().split())
completion = list(input().split())




