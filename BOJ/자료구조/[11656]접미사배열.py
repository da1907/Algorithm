str = input()
new_str = []

#0~끝, 1~끝, 1~끝,... 해준 문자열을 new_str에 추가해준다
for i in range(len(str)):
    new_str.append(str[i:len(str)])

#사전순 정렬
new_str.sort()

#출력
for i in new_str:
    print(i)
