def fun():
    arr = []

    a = int(input("수를 입력하세요 : "))

    for i in range(a):
        arr.append(int(input()))

    arr.sort()

    print(arr[:])
