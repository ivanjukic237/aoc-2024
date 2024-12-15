from enum import Enum


class Orientation(Enum):
    HORIZONTAL = 1
    VERTICAL = 2


class Node:
    def __init__(self, coordinates, name):
        self.value = 4
        self.coordinates = coordinates
        self.name = name

    top = None
    bottom = None
    right = None
    left = None

    def __repr__(self):
        return f" name: {self.name} value: {self.value} {self.coordinates}"

    def __hash__(self):
        return hash(self.coordinates)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.coordinates == other.coordinates
        return False


unvisited_nodes = set()
visited_nodes = set()
one_set_nodes = set()
one_set_nodes_names = set()


def check(node, grid):
    global unvisited_nodes
    global visited_nodes

    unvisited_nodes.remove(node)
    visited_nodes.add(node)
    one_set_nodes.add(node)
    one_set_nodes_names.add((node.coordinates[0], node.coordinates[1]))
    x = node.coordinates[0]
    y = node.coordinates[1]

    num_of_nodes = 1
    value_of_nodes = 4

    if x + 1 < len(grid) and grid[y][x + 1].name == node.name:
        node.value -= 1
        value_of_nodes -= 1
        node.right = grid[y][x + 1]
        if grid[y][x + 1] not in visited_nodes:
            a = check(grid[y][x + 1], grid)
            num_of_nodes += a[0]
            value_of_nodes += a[1]

    if y + 1 < len(grid) and grid[y + 1][x].name == node.name:
        node.value -= 1
        value_of_nodes -= 1
        node.bottom = grid[y + 1][x]
        if grid[y + 1][x] not in visited_nodes:
            a = check(grid[y + 1][x], grid)
            num_of_nodes += a[0]
            value_of_nodes += a[1]

    if x - 1 >= 0 and grid[y][x - 1].name == node.name:
        node.value -= 1
        value_of_nodes -= 1
        node.left = grid[y][x - 1]
        if grid[y][x - 1] not in visited_nodes:
            a = check(grid[y][x - 1], grid)
            num_of_nodes += a[0]
            value_of_nodes += a[1]

    if y - 1 >= 0 and grid[y - 1][x].name == node.name:
        node.value -= 1
        value_of_nodes -= 1
        node.top = grid[y - 1][x]
        if grid[y - 1][x] not in visited_nodes:
            a = check(grid[y - 1][x], grid)
            num_of_nodes += a[0]
            value_of_nodes += a[1]

    return num_of_nodes, value_of_nodes


def check_part_2(nodes):
    sum_2 = 0
    global one_set_nodes_names
    for n in nodes:
        sum_start = sum_2
        # solo block
        if n.value == 4:
            sum_2 += 4
        # end block
        elif n.value == 3:
            sum_2 += 2
        elif n.value == 2:
            # corner block
            if not (n.right is not None and n.left is not None or n.top is not None and n.bottom is not None):
                if n.right is not None and n.top is not None:
                    if (n.coordinates[0] + 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] - 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
                elif n.right is not None and n.bottom is not None:
                    if (n.coordinates[0] + 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] - 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                elif n.left is not None and n.top is not None:
                    if (n.coordinates[0] - 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] + 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
                else:
                    if (n.coordinates[0] - 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] + 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
        # triple block
        elif n.value == 1:
            if n.left is not None and n.right is not None:
                if n.top is not None:
                    if (n.coordinates[0] - 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] + 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                if n.bottom is not None:
                    if (n.coordinates[0] - 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] + 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1

            if n.top is not None and n.bottom is not None:
                if n.right is not None:
                    if (n.coordinates[0] + 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] + 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
                if n.left is not None:
                    if (n.coordinates[0] - 1, n.coordinates[1] - 1) not in one_set_nodes_names:
                        sum_2 += 1
                    if (n.coordinates[0] - 1, n.coordinates[1] + 1) not in one_set_nodes_names:
                        sum_2 += 1
        # cross
        elif n.value == 0:
            cross_corners = 4
            if (n.coordinates[0] + 1, n.coordinates[1] - 1) in one_set_nodes_names:
                cross_corners -= 1
            if (n.coordinates[0] + 1, n.coordinates[1] + 1) in one_set_nodes_names:
                cross_corners -= 1
            if (n.coordinates[0] - 1, n.coordinates[1] - 1) in one_set_nodes_names:
                cross_corners -= 1
            if (n.coordinates[0] - 1, n.coordinates[1] + 1) in one_set_nodes_names:
                cross_corners -= 1
            sum_2 += cross_corners

        # diagonal
        if n.value != 3:
            if ((n.coordinates[0] + 1, n.coordinates[1]) not in one_set_nodes_names and
                    (n.coordinates[0] + 1, n.coordinates[1] + 1) in one_set_nodes_names and (
                            n.coordinates[0], n.coordinates[1] + 1) not in one_set_nodes_names):
                sum_2 += 1

            if ((n.coordinates[0] - 1, n.coordinates[1]) not in one_set_nodes_names and
                    (n.coordinates[0] - 1, n.coordinates[1] - 1) in one_set_nodes_names and (
                            n.coordinates[0], n.coordinates[1] - 1) not in one_set_nodes_names):
                sum_2 += 1

            if ((n.coordinates[0] - 1, n.coordinates[1]) not in one_set_nodes_names and
                    (n.coordinates[0] - 1, n.coordinates[1] + 1) in one_set_nodes_names and
                    (n.coordinates[0], n.coordinates[1] + 1) not in one_set_nodes_names):
                sum_2 += 1

            if ((n.coordinates[0] + 1, n.coordinates[1]) not in one_set_nodes_names and
                (n.coordinates[0] + 1, n.coordinates[1] - 1) in one_set_nodes_names and
                (n.coordinates[0], n.coordinates[1] - 1) not in one_set_nodes_names):
                sum_2 += 1

    return sum_2


if __name__ == "__main__":

    grid = []
    with open("day12.txt", "r") as file:
        for y, line in enumerate(file):
            line = line.strip()
            row = []
            for x, character in enumerate(line):
                node = Node((x, y), character)
                unvisited_nodes.add(node)
                row.append(node)
            grid.append(row)

        # print(unvisited_nodes)
        # print(grid)

        s = 0
        s_2 = 0
        while len(unvisited_nodes) != 0:
            a = check(next(iter(unvisited_nodes)), grid)
            s += a[0] * a[1]
            s_2 += a[0] * check_part_2(one_set_nodes)
            one_set_nodes = set()
            one_set_nodes_names = set()

        # print(visited_nodes)
        print(s)
        print(s_2)
