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

def shortest_wire(intersections, w1co, w2co):
    answ1 = []
    answ2 = []
    w1 = enumerate(w1co)
    w2 = enumerate(w2co)
    for x, y in intersections:
        ls_xy = [x, y]
        if ls_xy in w1co:
            answ1.append(w1co.index(ls_xy) + 1)
            # print(w1co.index(ls_xy))
        if ls_xy in w2co:
            answ2.append(w2co.index(ls_xy) + 1)
            # print(w2co.index(ls_xy))
    ans = min(x + y for x, y in zip(answ1, answ2))
    return ans
    


if __name__ == "__main__":
    # with open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday3.txt", "r") as f:
    with open ("inputday3.txt", "r") as f:
        f_read = f.read().split("\n")
        f_read.pop()
    w1 = f_read[0].split(",")
    w2 = f_read[1].split(",")
    # w1 = "R75,D30,R83,U83,L12,D49,R71,U7,L72".split(",")
    # w2 = "U62,R66,U55,R34,D71,R55,D58,R83".split(",")
    w1co = wire_coordinates(w1)
    w2co = wire_coordinates(w2)
    w1coset = make_set(w1co)
    w2coset = make_set(w2co)
    intersection = w1coset&w2coset
    print(shortest_wire(intersection, w1co, w2co))
