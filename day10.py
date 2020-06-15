'''Advent of code 2019 day10'''

import numpy as np

with open("inputday10.txt", "r") as f:
    f_read = f.read().split("\n")

class Point():
    def __init__(self,x ,y):
        self.x = x
        self.y = y

# def station_location(field): # ask the Liam what he would do for assigning points to every position
#     asteroid_field = field.copy()
#     y = 0
#     for i in asteroid_field:
#         for x in range(len(i)):
#             i[x] = Point(x, y)
#         y += 1
#     return asteroid_field

def station_location(field): 
    asteroid_field = field.copy()
    asteroid_points = []
    location_count = {}
    angles = [] #Idea: for each point hekc the angle to each other asteroid and store, if angle already stored don't count asteroid
    y = 0
    for i in asteroid_field:
        for x in range(len(i)):
            if i[x] == "#":
                asteroid_points.append(Point(x, y))
        y += 1
    for i in asteroid_points:
        for j in asteroid_points:
            if i == j:
                continue
            location_count[f"{i.x}, {i.y}"] = 0
            angle = np.arctan((i.y - j.y)/(i.x - j.x))
            if angle not in angles:
                angles.append(angle)
                location_count[f"{i.x}, {i.y}"] += 1
    ans = max(location_count.values())
    return ans

if __name__ == "__main__":
    print(station_location(f_read))


