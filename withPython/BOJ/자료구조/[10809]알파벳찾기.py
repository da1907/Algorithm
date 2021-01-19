alphabet = [[alpha, 0] for alpha in 'abcdefghijklmnopqrstuvwxyz']
word = input()

#단어의 뒤에서부터 앞으로 가면서 알파벳과 단어 철자가 같으면 단어의 인덱스를 알파벳과 세트인 숫자에 넣어줌
for i in alphabet:
    for j in range(len(word)-1,-1,-1):
        if i[0] == word[j]:
            i[1] = j

#알파벳과 세트인 수가 0인것들은 전부 -1로 바꾸어 줌
for i in alphabet:
    if i[1] == 0:
        i[1] -= 1

#단어의 인덱스가 0이었던것도 위에서 바뀌었으므로 단어의 인덱스 0인것은 다시 +1
for i in alphabet:
    if i[0] == word[0]:
        i[1] += 1

#출력
for i in alphabet:
    print(i[1], end = ' ')