class Hypothesis4:
    def encrypt(self, word):
        print("Word you want to encrypt: ", word)
        new_word = ""
        for i in range(len(word)):
            encode = (ord(word[i]) + 1)

            if encode > 122:
                encode -= 26

            new_word += chr(encode)

        return new_word


hypothesis = Hypothesis4()
print("Your encrypted word: ", hypothesis.encrypt("school"))
