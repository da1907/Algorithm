sen = input()

for ch in sen:
    if '0' <= ch <= '9':
        ch = ch
    else:
        ord(ch) = ord(ch) + 13

print(sen)