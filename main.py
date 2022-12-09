alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m",
            "n", "o", "p", "r", "s", "t", "u", "w", "y", "z"]


for alphabet in range(len(alphabet)):
    alphabet[0] = alphabet[[0] + 1]

print(alphabet)