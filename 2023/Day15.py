if __name__ == "__main__":
    num = 0
    with open("day15.txt", "r") as file:
        for line in file:
            line = line + ","
            a = 0
            for character in line:
                if character == ",":
                    num += a
                    a = 0
                    continue
                acii_value = ord(character)
                a += acii_value
                a = a * 17
                a = a % 256
    print(num)


class Lens:
    def __init__(self, mark, number, full_name):
        self.mark = mark
        self.number = number
        self.full_name = full_name

    def __repr__(self):
        return f"{self.full_name}"


if __name__ == "__main__":
    num = 0
    array = [[] for _ in range(255)]
    name_array = [[] for _ in range(255)]
    with open("day15.txt", "r") as file:
        for line in file:
            arr = line.split(",")
            for k in arr:
                a = 0
                delimiter = ""
                if "-" in k:
                    delimiter = "-"
                else:
                    delimiter = "="
                for letter in k.split(delimiter)[0]:
                    acii_value = ord(letter)
                    a += acii_value
                    a = a * 17
                    a = a % 256

                mark = k.split(delimiter)[0]
                if delimiter == "-":
                    if mark in list(map(lambda x: x.mark, array[a])):
                        a = 0
                        array[a] = [x for x in array[a] if x.mark != mark]
                else:
                    array[a].append(Lens(k.split(delimiter)[0], int(k.split(delimiter)[1]), k))

    print(array)


