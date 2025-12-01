from math import ceil


def part1():
    with open("day1.txt", 'r') as file:
        index = 50
        count = 0
        for line_number, line in enumerate(file, start=1):
            if line[0] == 'R':
                index = (int(line[1:]) + index) % 100
            else:
                index = 100 - (int(line[1:]) - index) % 100

            index = abs(index)

            if index == 100:
                index = 0

            if index == 0:
                count += 1

        print(count)


def part2():
    with open("day1.txt", 'r') as file:
        index = 50
        count = 0
        for line_number, line in enumerate(file, start=1):
            line_number = int(line[1:])
            if line[0] == 'R':
                count += int((index + line_number) / 100)
                index = (line_number + index) % 100
            else:
                real_index = index - line_number
                # guaranteed to pass 0 once, if we were at 0 we didn't pass it
                if index != 0 and real_index <= 0:
                    count += 1
                count += abs(int((index - line_number) / 100))

                index = (index - line_number) % 100

            index = abs(index)

            if index == 100:
                index = 0
        print(count)

if __name__ == "__main__":
    part1()
    part2()