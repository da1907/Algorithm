def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book)-1):
        if phone_book[i] == phone_book[i+1]:
                return False
        if phone_book[i] in phone_book[i+1]:
                return False

    return True

phone_book = []
for i in range(3):
    phone_book.append(input())

if solution(phone_book):
    print("true")
else:
    print("false")