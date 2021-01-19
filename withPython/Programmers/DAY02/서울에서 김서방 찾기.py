#내가 푼 것
def solution(seoul):
    answer = ''

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            num = i

    answer = "김서방은 %d에 있다." %num

    return answer

#-------------------------
def solution(seoul):
    return "김서방은 {}에 있다".format(seoul.index('Kim'))