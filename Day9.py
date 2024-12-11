def sum_of_consecutive(a, b):
    return int(((b - a + 1) / 2) * (a + b))


if __name__ == "__main__":
    with open("day9.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = [int(char) for char in line]
            suma = 0
            value_of_position = 0
            i_forward = 1
            i_backward = len(line) - 1
            is_unmovable_block = True
            while i_forward < len(line) and i_backward >= 0:
                # print("VALUE OF POSITION: " + str(value_of_position))

                if is_unmovable_block:
                    already_good_index = (i_forward - 1) / 2
                    suma += int(already_good_index * sum_of_consecutive(value_of_position,
                                                                        value_of_position + line[i_forward - 1] - 1))
                    value_of_position += line[i_forward - 1]
                # print("good VALUE OF POSITION: " + str(value_of_position))
                if i_forward > i_backward:
                    break
                to_move = line[i_backward]
                to_move_index = i_backward / 2

                capacity = line[i_forward]

                num_left = to_move - capacity

                if num_left > 0:
                    suma += int(to_move_index * sum_of_consecutive(value_of_position, value_of_position + capacity - 1))
                    line[i_backward] = num_left
                    value_of_position += capacity
                    i_forward += 2
                    is_unmovable_block = True
                elif num_left < 0:
                    suma += int(to_move_index * sum_of_consecutive(value_of_position, value_of_position + to_move - 1))
                    line[i_forward] = - num_left
                    value_of_position += to_move
                    i_backward -= 2
                    is_unmovable_block = False
                else:
                    suma += int(to_move_index * sum_of_consecutive(value_of_position, value_of_position + to_move - 1))
                    value_of_position += to_move
                    line[i_forward] = 0
                    i_forward += 2
                    i_backward -= 2
                    is_unmovable_block = True

            print(suma)


class AocSpace:
    def __init__(self, identificator, size, size_empty):
        self.identificator = identificator
        self.size = size
        self.size_empty = size_empty
        self.files = []

    identificator = 0
    size = 0
    size_empty = 0
    empty = False
    files = []
    moved = False

    def __repr__(self):
        return f"id:{self.identificator} size:{self.size} size_empty:{self.size_empty} "

    def is_empty(self):
        return self.size == 0


# part 2
if __name__ == "__main__":
    arr = []
    with open("day9.txt", "r") as file:
        for line in file:
            line = line.strip()
            line = [int(char) for char in line]

            #print(line)

            count = 0
            for index, pos in enumerate(line):
                if index % 2 == 0:
                    arr.append(AocSpace(count, pos, 0))
                    count += 1
                else:
                    arr.append(AocSpace(count * 10, 0, pos))

            #print(arr)

            index_1 = 1
            index_2 = len(arr) - 1

            while index_2 >= 0 and index_1 < len(arr):
                file_1 = arr[index_1]
                file_2 = arr[index_2]

                if file_1.size_empty >= file_2.size:
                    file_1.size_empty = file_1.size_empty - file_2.size
                    file_1.files.append(file_2)
                    file_2.moved = True
                    index_2 -= 2
                    index_1 = 1
                    continue

                if index_1 >= index_2:
                    index_2 -= 2
                    index_1 = 1
                    continue
                index_1 += 2

            #print(arr)

            sumaaaaaa = 0
            counter = 0
            for index, a in enumerate(arr):
                if index % 2 == 0:
                    if not a.moved:
                        for i in range(a.size):
                            #print(a.identificator, end="")
                            sumaaaaaa += counter * a.identificator
                            counter += 1
                    else:
                        for i in range(a.size):
                            #print(".", end="")
                            counter += 1

                else:
                    for k in a.files:
                        for k1 in range(k.size):
                            #print(k.identificator, end="")
                            sumaaaaaa += counter * k.identificator
                            counter += 1
                    for k2 in range(a.size_empty):
                        #print(".", end="")
                        counter += 1

            print()
            print(counter)
            print(sumaaaaaa)
