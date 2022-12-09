word = "kaszanka"


for i in range(len(word)):
    print(ord(word[i]))


print()


for i in range(len(word)):
    zaszyfrowane = (ord(word[i]) + 1)

    if zaszyfrowane > 122:
        zaszyfrowane -= 26

    print(chr(zaszyfrowane))