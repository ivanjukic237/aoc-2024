from functools import lru_cache

max_num = 75


class Node:
    def __init__(self, value, parent):
        self.value = value
        self.children = []
        self.parent = parent

    def __repr__(self):
        return f" {self.value}"

    def __hash__(self):
        return hash(self.value)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.value == other.value
        return False


@lru_cache(maxsize=None)
def calculate_num_of_children(node, index):
    if index == max_num:
        return 0

    str_value = str(node.value)
    if node.value == 0:
        node.children.append(Node(1, node))
    elif len(str_value) % 2 == 0:
        node.children.append(Node(int(str_value[0:int(len(str_value) / 2)]), node))
        node.children.append(Node(int(str_value[int(len(str_value) / 2):]), node))
    else:
        node.children.append(Node(node.value * 2024, node))

    index += 1
    sumica = 0
    for child in node.children:
        sumica += calculate_num_of_children(child, index)

    return sumica + len(node.children) - 1


if __name__ == "__main__":
    with open("day11.txt", "r") as file:
        for line in file:
            line = [int(char) for char in line.split()]
            suma = 0
            for c in line:
                root = Node(c, None)
                suma += calculate_num_of_children(root, 0)

            print(suma + len(line))