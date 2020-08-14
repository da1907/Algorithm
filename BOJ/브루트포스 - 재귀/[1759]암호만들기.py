L, C = map(int, input().split())
alpha = list(map(str, input().split()))     #사용 가능한 알파벳
alpha.sort()    #오름차순으로 사용하기 때문에 정렬해줌
out, out_all = [], []

def solve(depth, idx, L, C):
    if depth == L:  #depth와 L이 같으면 원하는 수만큼 방문 다 한것이므로 종료
        out_all.append(''.join(map(str, out)))     #out에 추가되어있는 문자들을 out_all에 추가해줌
        return

    for i in range(idx, C):     #depth와 L이 같지않으면
        out.append(alpha[i])    #해당 알파벳 out에 추가
        solve(depth+1, i+1, L, C)   #재귀
        out.pop()   #out에 저장되어있는 문자 지워줌

def compare(out_all):  #모음과 자음 갯수 세어주기 위한 함수
    for i in out_all:  #받아온 리스트의 문자 하나씩 꺼내
        cons = 0    #모음 갯수
        vow = 0     #자음 갯수
        for j in i:
            if j in 'aeiou':    #aeiou중에 있으면 모음 1증가
                cons += 1
            else:
                vow += 1

        if cons >= 1 and vow >= 2:  #모음이 한개 이상이고 자음이 두개 이상인 문자열만 출력
            print(i)
    return

solve(0, 0, L, C)
compare(out_all)