def solution(answers):
    #수포자 정답 패턴
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]

    scores = [0,0,0]    #수포자 1,2,3별로 정답 맞춘 갯수 넣을 배열 선언
    result = []     #최다득점자 넣을 배열

    #정답 배열과 수포자들의 답 비교해 맞으면 해당 scores배열의 요소 +1
    for i in range(len(answers)):
        if(answers[i] == p1[i%5]):
            scores[0] += 1
        if (answers[i] == p2[i%8]):
            scores[1] += 1
        if (answers[i] == p3[i%10]):
            scores[2] += 1

    #최다 득점 수 highest에 저장
    highest = max(scores)

    #최다 득점 수와 해당 수포자의 득점 수 같으면 result 배열에 추가해줌
    for i in range(3):
        if highest == scores[i]:
            result.append(i+1)

    return result
