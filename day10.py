'''Advent of code 2019 day10 This one got me and the solution here really helped me to understand
some extra functions from dictionaries that I didn't know https://github.com/Randdalf/aoc19/blob/master/d10.py'''

import numpy as np
import math
from collections import defaultdict

with open("inputday10.txt", "r") as f:
    f_read = f.read().split("\n")


class Point():
    def __init__(self,x ,y):
        self.x = int(x)
        self.y = int(y)


def station_location(field): 
    asteroid_field = field #field.copy()
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
    print(location)
    return ans, location, asteroid_points

def asteroid_bet(field):
    _, location, asteroid_points = station_location(field) #Location = 20,18
    location = Point(int(location.split(",")[0]), int(location.split(",")[1]))
    angles = defaultdict(list)

    for asteroid in asteroid_points:
        angles[angle(location, asteroid)].append(asteroid)

    world = list(angles.items())
    world.sort(key = lambda x: x[0])

    for _, asteroids in world:
        asteroids.sort(key = lambda x: distance(location, x))
    
    start = np.pi / 2
    index = 0
    while world[index][0] < start:
        index += 1
    
    dust = []
    while len(dust) < 200:
        asteroids = world[index][1]
        if len(asteroids) > 0:
            dust.append(asteroids.pop())
        index = (index + 1) % len(world)
    hecking_200th_asteroid = dust[-1]
    return (hecking_200th_asteroid.x * 100) + (hecking_200th_asteroid.y)
    
def distance(location, asteroid):
    return ((location.x - asteroid.x)**2 + (location.y - asteroid.y)**2)**0.5

def angle(location, asteroid):
    angle = np.arctan2((location.y - asteroid.y),(location.x - asteroid.x))
    return angle

if __name__ == "__main__":
    # print(station_location(f_read)[:2])
    print(asteroid_bet(f_read))