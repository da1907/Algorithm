import sys
sen = []

case = int(input())

for i in range(case):
    sen.append(sys.stdin.readline().strip().split())

    for j in range(len(sen[i])):
        print(''.join(reversed(sen[i][j])), end=' ')
"""

case = int(input())

for words in [list(map(lambda x: x[::-1], input().split())) for _ in range(case)]:
    print(*words)

"""

#string에 관련된 함수는 대부분 빅오가 크다
#스택 함수는 빅오1이므로 스택 사용!!
# =>push하다가 공백을 만나면 pop하게
#while안에 for문 쓰는것은 지양,,
#while True는 최대한 하지않기