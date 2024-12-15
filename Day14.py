import matplotlib
from scipy.stats import entropy

matplotlib.use('TkAgg')
from functools import reduce
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Button

width = 101
height = 103



class Node:
    def __init__(self, position, velocity):
        self.position = position
        self.velocity = velocity

    def __repr__(self):
        return f" {self.position}"

    def move(self):
        if self.position[0] + self.velocity[0] >= width:
            self.position[0] = (self.position[0] + self.velocity[0]) - width
        elif self.position[0] + self.velocity[0] < 0:
            self.position[0] = width + (self.position[0] + self.velocity[0])
        else:
            self.position[0] += self.velocity[0]

        if self.position[1] + self.velocity[1] >= height:
            self.position[1] = (self.position[1] + self.velocity[1]) - height
        elif self.position[1] + self.velocity[1] < 0:
            self.position[1] = height+ (self.position[1] + self.velocity[1])
        else:
            self.position[1] += self.velocity[1]


arr = []

if __name__ == "__main__":
    with open("day14.txt", "r") as file:
        for line in file:
            line = line.strip()
            a = line.split()
            pos = a[0].split(",")
            vel = a[1].split(",")
            arr.append(Node([int(pos[0][2:]), int(pos[1])], [int(vel[0][2:]), int(vel[1])]))

    fig, ax = plt.subplots()
    plt.subplots_adjust(bottom=0.2)
    line, = ax.plot([], [], 'o')
    ax.set_xlim(0, 150)
    ax.set_ylim(0, 150)
    ax.legend()
    step = 0
    def update_graph(event):
        global line
        global step

        x_arr = []
        y_arr = []
        print("ASDAS")
        for i in range(5000):
            print(i)
            step += 1
            for k_1 in arr:
                k_1.move()
                x_arr.append(k_1.position[0])
                y_arr.append(k_1.position[1])

            x_normalized = x_arr / np.sum(x_arr)
            y_normalized = y_arr / np.sum(y_arr)

            x_entropy = entropy(x_normalized)
            y_entropy = entropy(y_normalized)

            #print(f"x entropy: {x_entropy}")
            #print(f"y entropy: {y_entropy}")

            if x_entropy > 6.1 and y_entropy > 6.1:
                print(step)
                break
            x_arr = []
            y_arr = []

        line.set_data(np.array(x_arr), np.array(y_arr))
        line.set_label(f"{step}. sekunda")
        ax.legend()
        plt.draw()

    ax_button = plt.axes([0.4, 0.05, 0.2, 0.075])
    btn = Button(ax_button, 'Sljedeća iteracija')
    btn.on_clicked(update_graph)
    plt.show()

    for i in range(100):
        for k in arr:
            k.move()

    q = [0, 0, 0, 0]
    for k in arr:
        print(int(height / 2))
        if 0 <= k.position[0] < int(width / 2) and 0 <= k.position[1] < int(height / 2):
            q[0] += 1
        elif int(width / 2) < k.position[0] < width and 0 <= k.position[1] < int(height / 2):
            q[1] += 1
        elif 0 <= k.position[0] < int(width / 2) and int(height / 2) < k.position[1] < height:
            q[2] += 1
        elif width / 2 < k.position[0] < width and height / 2 < k.position[1] < height:
            q[3] += 1
    print(q)
    print(reduce(lambda x, y: x * y, q))
