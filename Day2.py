if __name__ == "__main__":
    count = 0
    with open("day2.txt", "r") as file:
        for line in file:
            lista = list(map(int, line.split()))
            asc = True
            if lista[0] > lista[1]:
                asc = False

            is_good = False
            already_skipped = False
            for i in range(len(lista) - 1):
                if lista[i + 1] > lista[i] and asc or lista[i + 1] < lista[i] and not asc:
                    if abs(lista[i + 1] - lista[i]) <= 3:
                        is_good = True
                    else:
                        if not already_skipped:
                            i += 2
                            already_skipped = True
                            continue
                        is_good = False
                        break
                else:
                    if not already_skipped:
                        i += 2
                        already_skipped = True
                        continue
                    is_good = False
                    break

            if is_good:
                print(lista)
                count += 1

    print(count)
