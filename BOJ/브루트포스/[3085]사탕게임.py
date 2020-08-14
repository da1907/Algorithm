import sys
m = []
n = int(input())
ans = 0

for i in range(n):
    m.append(list(map(str, sys.stdin.readline())))

#줄 별로 최대 몇개의 사탕이 같은지 확인하는 함수
def check():
    ans = 1             #함수에 들어올 때마다 ans는 1로 초기화 해주기
    cnt = 1             #각 행 비교해줄 때마다 cnt 1로 초기화

    for i in range(n):          #행별 비교 (가로비교 for문)
        for j in range(1, n):           #열별 비교
            #print('#', i,j)
            if m[i][j] == m[i][j-1]:        #붙어있는 옆칸이 같은 문자라면
                cnt += 1                #먹을수 있는 사탕이므로 cnt에 1 더하기
            else:               #옆칸 다른 문자라면
                ans = max(ans, cnt)         #ans와 cnt중 큰 값 저장
                cnt = 1
        #ans = max(ans, cnt)             #매 행마다 저장된 큰 값을 갱신해줌
        cnt = 1


    for i in range(n):          #위의 for문이 가로 비교였다면 이번 for문은 세로비교
        for j in range(1, n):
            #print('##', i,j)
            if m[j][i] == m[j-1][i]:
                cnt += 1

            else:
                ans = max(ans, cnt)
                cnt = 1
        #ans = max(ans, cnt)
        cnt = 1

    return ans  #최종 ans를 반환


#인접한 칸끼리 사탕 교환해주는 반복문
for i in range(n):
    for j in range(1, n):
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]     #양옆칸끼리 사탕을 교환하고
        ans = max(ans, check())        #check 함수에 넣어 ans를 반환받으면
        m[i][j], m[i][j-1] = m[i][j-1], m[i][j]     #다시 사탕 원래자리에 놔줌

        m[j][i], m[j-1][i] = m[j-1][i], m[j][i]     #위아래칸끼리 사탕 교환
        ans = max(ans, check())              #check 함수에 넣어 ans를 반환 받으면
        m[j][i], m[j-1][i] = m[j-1][i], m[j][i]     #다시 사탕 원래자리에 놔줌

print(ans)
