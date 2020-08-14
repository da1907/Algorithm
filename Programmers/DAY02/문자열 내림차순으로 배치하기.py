def solution(s):
    list = sorted(s, reverse = True)
    s = "".join(list)

    return s

#--------------------------------
def solution(s):
    list = sorted(s, reverse=True)
    answer = ''

    for i in list:
        answer = answer + i

    return answer

#역순으로 정렬하는 것 까지는 했는데
#그대로 return 하면 리스트 자체가 리턴되어서 [g,f,e,d] 이런식으로 반환된다
#리스트를 문자열로 바꾸는 방법이나 반복문을 통해 하나씩 추가시키는 법 배워가기!!
