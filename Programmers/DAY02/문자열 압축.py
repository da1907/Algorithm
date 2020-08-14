def solution(s):
    n = 0
    str = ''

    for i in range(1,len(s)):
        str = s[n:i]
        if str[n] ==