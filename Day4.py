if __name__ == "__main__":
    matrica = []
    with open("day4.txt", "r") as file:
        for line in file:
            a = []
            for letter in line:
                if letter != "\n":
                    a.append(letter)
            matrica.append(a)

    # print(matrica)
    good_words = ["XMAS", "SAMX"]
    count = 0
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if matrica[i][j] in ["X", "S"]:
                word = ""
                if j + 3 < len(matrica):
                    for forward in range(j, j + 4):
                        word += matrica[i][forward]
                if word in good_words:
                    #print("desno", i, j)
                    count += 1

                word = ""
                if i + 3 < len(matrica) and j + 3 < len(matrica):
                    for forward_j, forward_i in zip(range(j, j + 4), range(i, i + 4)):
                        word += matrica[forward_i][forward_j]
                    if word in good_words:
                        #print("desno dolje", i, j)
                        count += 1

                word = ""
                if j - 3 >= 0 and i + 3 < len(matrica):
                    for forward_i, forward_j in zip(range(i, i + 4), range(j, j - 4, -1)):
                        word += matrica[forward_i][forward_j]
                    if word in good_words:
                        #print("lijevo dolje", i, j)
                        count += 1

                word = ""
                if i + 3 < len(matrica):
                    for forward_i in range(i, i + 4):
                        word += matrica[forward_i][j]
                    if word in good_words:
                        #print("dolje",i, j)
                        count += 1
    print(count)


if __name__ == "__main__":
    matrica = []
    with open("day4.txt", "r") as file:
        for line in file:
            a = []
            for letter in line:
                if letter != "\n":
                    a.append(letter)
            matrica.append(a)

    count = 0
    for i in range(len(matrica)):
        for j in range(len(matrica[i])):
            if matrica[i][j] == "A":
                if i - 1 >= 0 and i + 1 < len(matrica) and j - 1 >= 0 and j + 1 < len(matrica):
                    if matrica[i - 1][j - 1] + matrica[i + 1][j + 1] in ["MS", "SM"] and matrica[i + 1][j - 1] + matrica[i - 1][j + 1] in ["MS", "SM"]:
                        count += 1
                        print(i, j)

    print(count)
