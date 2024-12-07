class Node:

    def __init__(self, value, type, children):
        self.value = value
        self.children = children
        self.type = type

    def __repr__(self):
        return f"Node(value={self.value}, type={self.type})"

    def pretty_print(self, level=0):
        indent = "  " * level
        result = f"{indent}- {self.value} ({self.type})\n"
        for child in self.children:
            result += child.pretty_print(level + 1)
        return result

    value = 0
    children = []
    type = ""


def recursion(node, values, main_value, i):
    if i >= len(values):
        if node.value == main_value:
            return True
        return False
    if main_value < node.value:
        return False

    value = values[i]

    add_nodes(node, value)

    return (recursion(node.children[0], values, main_value, i + 1) or
            recursion(node.children[1], values, main_value, i + 1) or
            (recursion(node.children[2], values, main_value, i + 1))
            )


def add_nodes(current_node, value):
    value_plus = current_node.value + value
    value_times = current_node.value * value

    new_node_plus = Node(value_plus, "+", [])
    new_node_times = Node(value_times, "*", [])
    new_node_concat = Node(int(str(current_node.value) + str(value)), "||", [])

    current_node.children.append(new_node_plus)
    current_node.children.append(new_node_times)
    current_node.children.append(new_node_concat)


# optimizirati, ne uzimati one koj su u prvom dijelu uspjeli
if __name__ == "__main__":
    count = 0
    with open("day7.txt", "r") as file:
        for line in file:
            line = line.strip()
            input = line.split(":")
            first = int(input[0])
            second = list(map(int, input[1].split()))

            root = Node(second[0], "M", [])

            is_ok = recursion(root, second[1:], first, 0)
            if is_ok:
                count += first
                #print(line)
                #print(root.pretty_print())
            # print(is_ok)

    print(count)
