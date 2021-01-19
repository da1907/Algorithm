import sys

def solution(x):
    sum = 0
    # 숫자 문자열로 변환
    tmp = str(x)
    # 숫자 한자리씩 꺼내서
    for i in range(len(tmp)):
        # 다시 숫자로 변환해서 더하기
        sum += int(tmp[i])
    if x % sum == 0:
        return True
    else:
        return False

tmp = []
x = int(sys.stdin.readline())

if solution(x):
    print("true")
else:
    print("false")