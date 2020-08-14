str = list(input())     #단어 입력받기
#각 알파벳과 그 갯수를 같이 받기위한 리스트 초기화
alphabet = [[alpha, 0] for alpha in 'abcdefghijklmnopqrstuvwxyz']

for i in alphabet:  #alphabet 리스트에 저장되어있는 순서대로
    for char in str:    #단어의 철자를 비교
        if i[0] == char:    #인덱스 0이므로 알파벳과 단어의 철자가 같으면
            i[1] += 1   #인덱스 1. 즉, 해당 알파벳의 갯수 1 증가

for i in alphabet:
    print(i[1], end = ' ')
