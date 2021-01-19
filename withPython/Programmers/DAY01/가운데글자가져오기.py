def solution(s):
    a = len(s)

    #글자 길이 짝수이면
    if a%2 == 0:
        return s[((a//2)-1):(a//2)+1]

    #글자 길이 홀수이면
    if a%2 != 0:
        return s[a//2]