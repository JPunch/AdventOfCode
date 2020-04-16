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
#  plt.show()
# plt.savefig('wires.png')


def wire_coordinates(wire): #Example input L12 "wire goes left by 12"
    currentpos = [0,0]
    coordinatelist = []

#    print(direction, magnitude)
    for instruction in wire:
        direction = re.sub('[0-9]','', instruction)
        magnitude = int(re.sub('[a-zA-Z]', "", instruction))
        if direction == "L":
            currentpos[0] -= magnitude
            coordinatelist.append(currentpos)
        elif direction == "R":
            currentpos[0] += magnitude
            coordinatelist.append(currentpos)
        elif direction == "U":
            currentpos[1] += magnitude
            coordinatelist.append(currentpos)
        elif direction == "D":
            currentpos[1] -= magnitude
            coordinatelist.append(currentpos)
        else:
            print("There is an incorrect direction")
    # print(coordinatelist)
    return coordinatelist


def intersection(wire1, wire2):
    list_intersections = []
    for coordinates1 in wire1:
        for coordinates2 in wire2:
            x = coordinates1[0] - coordinates2[0]
            y = coordinates1[1] - coordinates2[1]
            if x + y == 0:
                list_intersections.append((coordinates1))
    return list_intersections


def does_intersect(vert_wire_1, horiz_wire_1, vert_wire_2, horiz_wire_2):
    v_x1, v_y1 = vert_wire_1
    v_x2, v_y2 = vert_wire_2
    
    h_x1, h_y1 = horiz_wire_1
    h_x2, h_y2 = horiz_wire_2
ayyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy lmao
    if v_y1 <= h_y1 <= vy2 or v_y1 <= h_y2 <= vy2:
        if v_y1 <= h_y1 <= vy2 or v_y1 <= h_y2 <= vy2:
            pass

def closest_intersection(list_intersections):
    manhattan_distances = []
    def manhattan_distance(Coordinates):
        return Coordinates[0] + Coordinates[1]
    for intersections in list_intersections:
        manhattan_distances.append(manhattan_distance(intersections))
    print(manhattan_distances.sort())


if __name__ == "__main__":
    with open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday3.txt", "r") as f:
        f_read = f.read().split("\n")
        f_read.pop()
    w1 = f_read[0].split(",")
    w2 = f_read[1].split(",")

    w1co = wire_coordinates(w1)
    w2co = wire_coordinates(w2)

    intersection(w1co, w2co)
    #closest_intersection(intersection(wire_coordinates(w1), wire_coordinates(w2)))