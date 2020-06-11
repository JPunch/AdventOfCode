import matplotlib.pyplot as plt
import numpy as np
import re

# def wire_plotter(wire, filename): #Example input L12 "wire goes left by 12"
#     currentpos = [0,0]

#     for instruction in wire:
#         direction = re.sub('[0-9]','', instruction)
#         magnitude = int(re.sub('[a-zA-Z]', "", instruction))
#         print(direction, magnitude)

#         if direction == "L":
#             x = np.linspace(currentpos[0], currentpos[0] - magnitude)
#             y = np.linspace(currentpos[1], currentpos[1])
#             plt.plot(x, y, '-r', label='')
#             currentpos = [x[-1], y[-1]]
#         elif direction == "R":
#             x = np.linspace(currentpos[0], currentpos[0] + magnitude)
#             y = np.linspace(currentpos[1], currentpos[1])
#             plt.plot(x, y, '-r', label='')
#             currentpos = [x[-1], y[-1]]
#         elif direction == "U":
#             x = np.linspace(currentpos[0], currentpos[0])
#             y = np.linspace(currentpos[1], currentpos[1] + magnitude)
#             plt.plot(x, y, '-r', label='')
#             currentpos = [x[-1], y[-1]]
#         elif direction == "D":
#             x = np.linspace(currentpos[0], currentpos[0])
#             y = np.linspace(currentpos[1], currentpos[1] - magnitude)
#             plt.plot(x, y, '-r', label='')
#             currentpos = [x[-1], y[-1]]
#         else:
#             print("There is an incorrect direction")
#     plt.legend(loc='upper left')
#     plt.grid()
#     plt.savefig(filename)


# wire_plotter(w1, 'w1.png')
# wire_plotter(w2, 'w2.png')

# x = np.linspace(-5,5,100)
# y = 2*x+1
# plt.plot(x, y, '-r', label='')
# plt.title('Graph of y=2x+1')
# plt.xlabel('x', color='#1C2833')
# plt.ylabel('y', color='#1C2833')
# plt.legend(loc='upper left')
# plt.grid()
# plt.show()
# plt.savefig('wires.png')


def wire_coordinates(wire): #Example input L12 "wire goes left by 12"
    currentpos = [0,0]
    coordinatelist = []
    for instruction in wire:
        direction = re.sub('[0-9]','', instruction)
        magnitude = int(re.sub('[a-zA-Z]', "", instruction))
        if direction == "L":
            for _ in range(magnitude):
                currentpos[0] -= 1
                coordinatelist.append(currentpos[:])
        elif direction == "R":
            for _ in range(magnitude):
                currentpos[0] += 1
                coordinatelist.append(currentpos[:])
            # currentpos[0] += magnitude
            # coordinatelist.append(currentpos[:])
        elif direction == "U":
            for _ in range(magnitude):
                currentpos[1] += 1
                coordinatelist.append(currentpos[:])
            # currentpos[1] += magnitude
            # coordinatelist.append(currentpos[:])
        elif direction == "D":
            for _ in range(magnitude):
                currentpos[1] -= 1
                coordinatelist.append(currentpos[:])
            # currentpos[1] -= magnitude
            # coordinatelist.append(currentpos[:])
        else:
            print("There is an incorrect direction")
    return coordinatelist

def closest_intersection(w1co, w2co):
    intersection = [i for i in w1co if i in w2co]
    ans = min([abs(x) + abs(y) for (x, y) in intersection])
    return ans

def make_set(wire):
    wire_set = set()
    for i in wire:
        x = i[0]
        y = i[1]
        wire_set.add((x, y))
    return wire_set


if __name__ == "__main__":
    # with open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday3.txt", "r") as f:
    with open ("inputday3.txt", "r") as f:
        f_read = f.read().split("\n")
        f_read.pop()
    w1 = f_read[0].split(",")
    w2 = f_read[1].split(",")
    # w1 = "R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51".split(",")
    # w2 = "U98,R91,D20,R16,D67,R40,U7,R15,U6,R7".split(",")
    w1co = wire_coordinates(w1)
    w2co = wire_coordinates(w2)
    w1co = make_set(w1co)
    w2co = make_set(w2co)
    print(w1co&w2co)
    print(closest_intersection(w1co, w2co))