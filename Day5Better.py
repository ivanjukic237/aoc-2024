def add_to_dict(dic, v, i):
    if v in dic:
        dic[v] += i
    else:
        dic[v] = i


if __name__ == "__main__":
    rules = []
    updates = []
    with open("day5.txt", "r") as file:
        rule_flag = True
        for line in file:
            line = line.strip()
            if not line:
                rule_flag = False
                continue
            if rule_flag:
                rules.append(line.strip().split("|"))
            else:
                updates.append(line.strip().split(","))

    sum_1 = 0
    sum_2 = 0
    for update in updates:
        values = {}
        for rule in rules:
            if rule[0] in update and rule[1] in update:
                add_to_dict(values, rule[0], 1)
                add_to_dict(values, rule[1], - 1)

        update_copy = update.copy()
        known_numbers = []
        for index, u in enumerate(update):
            if u in values:
                known_numbers.append(u)
                update_copy[index] = None
        good_order = sorted(known_numbers, key=lambda item: values[item], reverse=False)

        for index, u in enumerate(update_copy):
            if u is None:
                update_copy[index] = good_order.pop()

        s = int(update_copy[int(len(update_copy) / 2)])
        if update_copy == update:
            sum_1 += s
        else:
            sum_2 += s

    print(sum_1)
    print(sum_2)
