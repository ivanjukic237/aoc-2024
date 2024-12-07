import re

if __name__ == "__main__":
    count = 0
    with open("day3.txt", "r") as file:
        data = file.read()
        matched = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)", data)
        print(matched)
        for m in matched:
            only_nums = m[4:-1].split(",")
            count += int(only_nums[0]) * int(only_nums[1])
    print(count)

# part2
if __name__ == "__main__":
    count = 0
    with open("day3.txt", "r") as file:
        data = file.read()
        matched = re.findall("mul\\(\\d{1,3},\\d{1,3}\\)|do\\(\\)|don't\\(\\)", data)
        print(matched)
        stopped = False
        for m in matched:
            if m == 'do()':
                stopped = False
                continue
            if m == 'don\'t()':
                stopped = True
                continue
            if not stopped:
                only_nums = m[4:-1].split(",")
                count += int(only_nums[0]) * int(only_nums[1])
    print(count)
