import sys
height = []

#아홉 난쟁이의 키 입력받기
for i in range(9):
    height.append(int(sys.stdin.readline()))

height.sort()
height_sum = sum(height)    #아홉난쟁이의 키 모두 더하기

for i in height:
    for j in height:
        if i == j: break    #같은 난쟁이의 키는 넘어감
        elif i + j == height_sum - 100:     #i 난쟁이와 j 난쟁이의 키가 전체난쟁이 키 - 100 과 같으면
            height.remove(i)    #i 난쟁이 제거
            height.remove(j)    #j 난쟁이도 제거

for i in height:
    print(i)