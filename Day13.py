import numpy as np
import pandas as pd


def cramer2x2(a, b):
    d = pd.det(a)
    dx = pd.det(np.column_stack([b, a[:, 1]]))
    dy = pd.det(np.column_stack([a[:, 0], b]))
    return np.array([dx/d, dy/d])


def solve_1(a, b, prize):
    solution = np.linalg.solve(np.array([a, b]), prize)

    print(solution)

    if len(solution) == 0:
        return 0
    k_1 = None
    k_2 = None

    asd = str(solution[1])[-2:]
    if str(solution[0])[-2:] == '.0':
        k_1 = solution[0]

    if str(solution[1])[-2:] == '.0':
        k_2 = solution[1]

    if k_1 is not None and k_2 is not None:
        return 3 * k_1 + k_2
    elif k_1 is not None:
        return 3 * k_1
    elif k_2 is not None:
        return k_2
    return 0


if __name__ == "__main__":

    a = []
    b = []
    prize = []
    suma = 0
    with open("day13.txt", "r") as file:
        i = 0
        for line in file:
            if i == 3:
                suma += solve_1(a, b, prize)
                a = []
                b = []
                prize = []
                i = 0
                continue
            line = line.strip()
            s = line.split(":")[1].split(",")
            sol = (int(s[0].strip()[2:]), int(s[1].strip()[2:]))

            if i != 2:
                a.append(sol[0])
                b.append(sol[1])
            if i == 2:
                prize.append(sol[0])
                prize.append(sol[1])

                #prize.append(int('10000000000000' + str(sol[0])))
                #prize.append(int('10000000000000' + str(sol[1])))
            i += 1

    print(suma)
