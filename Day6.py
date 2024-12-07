from enum import Enum
import copy


def rotate(orientation_1):
    if orientation_1 == GuardOrientation.TOP:
        return GuardOrientation.RIGHT
    elif orientation_1 == GuardOrientation.RIGHT:
        return  GuardOrientation.BOTTOM
    elif orientation_1 == GuardOrientation.BOTTOM:
        return GuardOrientation.LEFT
    else:
        return GuardOrientation.TOP


class GuardOrientation(Enum):
    TOP = 1
    BOTTOM = 2
    RIGHT = 3
    LEFT = 4

    def __repr__(self):
        return f"{self.name}"

if __name__ == "__main__":
    grid = []
    guard_postition = [0 for _ in range(2)]
    moves = []
    with open("day6.txt", "r") as file:
        for y, line in enumerate(file):
            line = line.strip()
            arr = []
            grid.append(arr)
            for x, character in enumerate(line):
                arr.append(character)
                if character == "^":
                    guard_postition[0] = x
                    guard_postition[1] = y

    #print(grid)
    begin_x = guard_postition[0]
    begin_y = guard_postition[1]
    initial_pos_x = guard_postition[0]
    initial_pos_y = guard_postition[1]
    print(guard_postition)
    grid_initial = copy.deepcopy(grid)
    orientation = GuardOrientation.TOP

    count = 0
    while True:
        move_x = guard_postition[0]
        move_y = guard_postition[1]

        if orientation == GuardOrientation.TOP:
            move_y -= 1
        elif orientation == GuardOrientation.BOTTOM:
            move_y += 1
        elif orientation == GuardOrientation.RIGHT:
            move_x += 1
        else:
            move_x -= 1

        if not (0 <= move_x < len(grid[0]) and 0 <= move_y < len(grid)):
            break

        if grid[move_y][move_x] == "#":
            orientation = rotate(orientation)
        else:
            guard_postition[0] = move_x
            guard_postition[1] = move_y
            #print(guard_postition)
            if grid[move_y][move_x] != "X":
                count += 1
            grid[move_y][move_x] = "X"
            moves.append([move_x, move_y, orientation])

    print(guard_postition)
    # brojimo prvi korak, ali ne ako je stražar prošao preko početne pozicije
    # jer je inače duplo
    if grid[begin_y][begin_x] != "X":
        count += 1
    print(count)

   # for row in grid:
   #     print("".join(map(str, row)))

   # print("\n")
   # for row in grid_initial:
   #     print("".join(map(str, row)))

    print(moves)


    count_2 = 0
    found_moves = []
    found_moves_only_xy = set()
    for move in moves:
        if str(move[0]) + " " + str(move[1]) in found_moves_only_xy:
            continue
        grid_copy = copy.deepcopy(grid_initial)
        grid_copy[move[1]][move[0]] = "#"

        guard_postition[0] = initial_pos_x
        guard_postition[1] = initial_pos_y

        begin_x = guard_postition[0]
        begin_y = guard_postition[1]
        orientation = GuardOrientation.TOP

        new_moves = []

        while True:
            move_x = guard_postition[0]
            move_y = guard_postition[1]

            if orientation == GuardOrientation.TOP:
                move_y -= 1
            elif orientation == GuardOrientation.BOTTOM:
                move_y += 1
            elif orientation == GuardOrientation.RIGHT:
                move_x += 1
            else:
                move_x -= 1

            if not (0 <= move_x < len(grid[0]) and 0 <= move_y < len(grid)):
                break

            if grid_copy[move_y][move_x] == "#":
                orientation = rotate(orientation)
            else:
                guard_postition[0] = move_x
                guard_postition[1] = move_y
                if grid_copy[move_y][move_x] != "X":
                    count += 1
                grid_copy[move_y][move_x] = "X"
                new_move = [move_x, move_y, orientation]
                if new_move in new_moves:
                    found_moves.append(move)
                    found_moves_only_xy.add(str(move[0]) + " " + str(move[1]))
                    print(move)
                    count_2 += 1
                    break
                else:
                    new_moves.append(new_move)

    print(count_2)
    print(found_moves)

    print(len(found_moves))