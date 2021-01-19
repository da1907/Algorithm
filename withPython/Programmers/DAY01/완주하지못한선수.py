def solution(participant, completion):
    participant.sort()
    completion.sort()

    for i in range(len(completion)):    #계속 len을 안붙여줘서 오류
        if participant[i] != completion[i]:
            return participant[i]

    return participant[-1]  #필요성을 몰라서 안붙이다가 답보고 알게됨
