'''Advent of code 2019 day10'''

import numpy as np
import math

with open("inputday10.txt", "r") as f:
    f_read = f.read().split("\n")


class Point():
    def __init__(self,x ,y):
        self.x = x
        self.y = y


def station_location(field): 
    asteroid_field = field.copy()
    asteroid_points = []
    location_count = {}
    angles = []
    y = 0
    for i in asteroid_field:
        for x in range(len(i)):
            if i[x] == "#":
                asteroid_points.append(Point(x, y))
        y += 1
    for i in asteroid_points:
        location_count[f"{i.x}, {i.y}"] = 0
        for j in asteroid_points:
            if i == j:
                continue
            else:
                angle = np.arctan2((i.y - j.y),(i.x - j.x))
                if angle not in angles:
                    angles.append(angle)
                    location_count[f"{i.x}, {i.y}"] += 1
        angles.clear()
    ans = max(location_count.values())
    for a in location_count:
        if location_count[a] == ans:
            location = a
    return ans, location, asteroid_points

def asteroid_bet(field):
    total, location, asteroid_points = station_location(field) #Location = 20,18
    location = Point(int(location.split(",")[0]), int(location.split(",")[1]))
    #so use ans to take away current amount of asteroids in sight then remove them and rerun until200th asteroid in sight and then sort to find it









    # angle = []
    # distances = []
    # locations = []
    # angle_distance = []
    # for j in asteroid_points:
    #     if location == j:
    #         continue
    #     else:
    #         angle.append([(180/np.pi)*np.arctan2((location.y - j.y),(location.x - j.x))])
    #         locations.append([j.x, j.y])
    #         distances.append([math.sqrt((location.x - j.x)**2 + (location.y - j.y)**2)])
    # for i in range(len(angle)):# I don't endorse the existence of this for loop or perhaps most of my for loops
    #     angle_distance.append((angle[i], distances[i])) 
    # # angle_distances = zip(angle, location) help me
    # angle_distance.sort(key = lambda x: x[1])
    # del angle_distance[0]
    # return angle_distance


#Idea a dictionary filled with angles and then distance from laser location(sorted)from first to last hit then loop through removing one from each angle in turn if dictionary is empty it is removed

if __name__ == "__main__":
    # print(station_location(f_read)[:2])
    print(asteroid_bet(f_read))