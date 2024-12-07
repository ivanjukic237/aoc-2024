from collections import Counter
if __name__ == "__main__":
    list1 = []
    list2 = []
    with open("day1.txt", "r") as file:
        for line in file:
            list1.append(int(line.split()[0]))
            list2.append(int(line.split()[1]))

    list1.sort()
    list2.sort()

    print(list1)
    suma = 0
    for item1, item2 in zip(list1, list2):
        suma += abs(item1 - item2)

    print(suma)

    mapa = Counter(list2)
    suma2 = 0
    for item1 in list1:
        if item1 in mapa:
            suma2 += item1 * mapa.get(item1)

    print(suma2)

