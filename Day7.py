import numpy


def get_perm(num, base, width):
    res = numpy.base_repr(num, base=base)
    res = '0' * (width - len(res)) + res
    return res


if __name__ == "__main__":
    count = 0
    with open("day7.txt", "r") as file:
        for line in file:
            line = line.strip()
            input = line.split(":")
            first = int(input[0])
            second = input[1].split()
            #print(first)
            #print(second)

            to = pow(2, (len(second) - 1))
            for i in range(0, to):
                perm = "0" + get_perm(i, 2, len(second) - 1)

                suma = 0

                for index, k in enumerate(perm):
                    if k == "0":
                        suma += int(second[index])
                    else:
                        suma *= int(second[index])

                    if suma > first:
                        break

                if suma == first:
                    count += first
                    print(line)
                    break
        print(count)

#1399219271639
#1399219271639