def solution(a,b):
    day = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    endDay = 0
    sum = 0

    if (a == 1 | a == 3 | a == 5 | a == 7 | a == 8 | a == 10 | a == 12) :
        endDay = 31

    elif a == 2:
        endDay = 29

    elif (a == 4 | a == 6 | a == 9 | a == 11) :
        endDay = 30

    for i in range(1, a):
        sum += endDay

    sum += b

    idx = b % 7

    return day[idx]