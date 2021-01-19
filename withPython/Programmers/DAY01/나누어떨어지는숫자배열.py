def solution(arr, divisor):
    result = []

    #arr배열 처음부터 divisor로 나누어 떨어지는 요소 있는지 검사 후 있으면 result 배열에 저장
    for i in range(len(arr)):
        if arr[i] % divisor == 0:
            result.append(arr[i])

    #result 배열의 길이 0이면 -1을 출력할 수 있도록 -1 추가
    if len(result) == 0:
        result.append(-1)

    return sorted(result)


