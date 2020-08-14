def solution(numbers):
    for i in range(len(numbers)):
        if numbers[i] < 10:
            k = numbers[i]

        elif (numbers[i] >= 10 | numbers[i] < 100):
            k = numbers[i] // 10

        elif (numbers[i] >= 100 | numbers[i] < 1000):
            k = numbers[i] // 100

    numbers.sort(key = lambda x : k)
    numbers.sort(reverse = True)

    for i in numbers:
        print(i, end='')

    return max