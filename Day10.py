from enum import Enum

positions_good_path = []
count = 0
solution = dict()

class From(Enum):
    TOP = 1
    BOTTOM = 2
    RIGHT = 3
    LEFT = 4

    def __repr__(self):
        return f"{self.name}"


def find_next_positions(grid, position):
    x = position[0]
    y = position[1]
    value = grid[y][x]
    next_positions = []

    if x + 1 < len(grid) and grid[y][x + 1] == value + 1:
        next_positions.append((x + 1, y, From.LEFT))

    if y + 1 < len(grid) and grid[y + 1][x] == value + 1:
        next_positions.append((x, y + 1, From.TOP))

    if x - 1 >= 0 and grid[y][x - 1] == value + 1:
        next_positions.append((x - 1, y, From.RIGHT))

    if y - 1 >= 0 and grid[y - 1][x] == value + 1:
        next_positions.append((x, y - 1, From.BOTTOM))

    return next_positions


def find_path(grid, starting_position, starting_position_index):
    global count
    global positions_good_path
    global solution
    if grid[starting_position[1]][starting_position[0]] == 9:
        if starting_position_index in solution.keys():
            solution[starting_position_index].add(starting_position[:2])
        else:
            s = set()
            s.add(starting_position[:2])
            solution[starting_position_index] = s
        count += 1
        return True

    if starting_position in positions_good_path:
        return True

    next_positions = find_next_positions(grid, starting_position)

    if len(next_positions) == 0:
        return False

    for p in next_positions:
        if find_path(grid, p, starting_position_index):
            positions_good_path.append(p)


if __name__ == "__main__":
    grid = []
    starting_positions = []
    with open("day10.txt", "r") as file:
        for y, line in enumerate(file):
            line = line.strip()
            row = []
            for x, c in enumerate(line):
                row.append(int(c))
                if c == '0':
                    starting_positions.append((x, y))
            grid.append(row)

        print(starting_positions)

        for index, p in enumerate(starting_positions):
            find_path(grid, p, index)
            print(count)

        print(count)
        print(solution)

        c = 0
        for k in solution.keys():
            for k1 in solution[k]:
                c += 1
        print(c)




