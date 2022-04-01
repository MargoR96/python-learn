word_1 = input()

while True:
    word_2 = input()
    if word_1[-1] == "ь":
        if word_1[-2] == word_2[0]:
            word_1 = word_2
            continue
    elif word_1[-1] == word_2[0]:
        word_1 = word_2
        continue
    else:
        print(word_2)
        break