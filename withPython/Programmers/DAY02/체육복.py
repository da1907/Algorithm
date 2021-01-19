#내가 푼 것
def solution(n, lost, reserve):

    for i in range(len(lost)):
        for j in range(len(reserve)):
            if lost[i] == reserve[j] - 1:
                del lost[i]
            if lost[i] == reserve[j] + 1:
                del lost[i]

        return n - len(lost)
34
#---------------------------------
#이 코드가 안되는 이유
#real_lost를 기준으로 하면, 첫번째 lost가 reserve에게 체육복을 빌리면
#해당 reserve는 더이상 여벌 체육복이 없는데
#다음 lost가 계산 했을 때 또 reserve가 걸리면 또 줘야하게 된다.
#따라서 lost 기준이 아닌 reserve를 기준으로 봐야함

def solution(n,lost,reserve):
    real_lost = [p for p in lost if p not in reserve]
    real_reserve = [p for p in reserve if p not in lost]

    for student in real_lost:
        if student - 1 in real_reserve:
            real_lost.remove(student)
        if student + 1 in real_reserve:
            real_lost.remove(student)

    return n - len(real_lost)

#-----------------------------------
def solution(n, lost, reserve):
    real_lost = [p for p in lost if p not in reserve]
    real_reserve = [p for p in reserve if p not in lost]

    for student in real_reserve:
        if student - 1 in real_lost:
            real_lost.remove(student - 1)
        elif student + 1 in real_lost:
            real_lost.remove(student + 1)

    return n - len(real_lost)