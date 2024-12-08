def add_antinode(antinodes, antinode, size):
    if 0 <= antinode[0] < size and 0 <= antinode[1] < size:
        antinodes.add(antinode)
        return True
    return False


def create_antinodes(n_1, n_2, antinodes, size, part_2, visited):
    x_1 = n_1[0] - n_2[0]
    y_1 = n_1[1] - n_2[1]

    x_2 = n_2[0] - n_1[0]
    y_2 = n_2[1] - n_1[1]

    a_1 = (n_1[0] + x_1, n_1[1] + y_1)
    a_2 = (n_2[0] + x_2, n_2[1] + y_2)

    if ((a_1, n_1) not in visited) and add_antinode(antinodes, a_1, size) and part_2:
        visited.add((a_1, n_1))
        create_antinodes(a_1, n_1, antinodes, size, part_2, visited)
    if ((a_2, n_2) not in visited) and add_antinode(antinodes, a_2, size) and part_2:
        visited.add((a_2, n_2))
        create_antinodes(a_2, n_2, antinodes, size, part_2, visited)


if __name__ == "__main__":
    mapa = dict()
    size = 0
    with open("day8.txt", "r") as file:
        for y, line in enumerate(file):
            line = line.strip()
            size = len(line)
            for x, c in enumerate(line):
                if c == ".":
                    continue
                if c in mapa:
                    mapa[c].append((x, y))
                else:
                    mapa[c] = [(x, y)]

    antinodes = set()
    visited = set()
    part_2 = True
    for c in mapa.keys():
        node = mapa[c]

        for i, n_1 in enumerate(node):
            for j, n_2 in enumerate(node[i + 1:]):
                create_antinodes(n_1, n_2, antinodes, size, part_2, visited)

    if part_2:
        for c in mapa.keys():
            node = mapa[c]
            for i in node:
                antinodes.add(i)

    print(len(antinodes))