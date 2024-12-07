import re


class Rule:
    rule = "",
    x = "",
    y = ""


def is_rule_ok(rul, lin):
    for r in rul:
        if re.search(r, lin):
            return False
    return True


def find_middle_num(lin):
    nums = lin.split(",")
    return int(nums[int(len(nums) / 2)])


def swap_words(s, x, y):
    return y.join(part.replace(y, x) for part in s.split(x))


if __name__ == "__main__":
    rules = []
    middle_num_sum_1 = 0
    file1 = open("MyFile.txt", "w")
    with open("day5.txt", "r") as file:
        rule_flag = True
        for line in file:
            line = line.strip()
            if not line:
                rule_flag = False
                continue
            if rule_flag:
                rule = line.strip().split("|")
                rules.append("(^|,){first}.*,{second}($|,)".format(first=rule[1], second=rule[0]))
            else:
                if is_rule_ok(rules, line):
                    middle_num_sum_1 += find_middle_num(line)
                else:
                    file1.write(line + '\n')

    print(middle_num_sum_1)



