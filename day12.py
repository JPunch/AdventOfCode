'''Advent of code 2019 day12 hopefully better thn day 10'''

import regex as re

def moon_parse(moons):
    moon_info = []
    moons = re.sub('[a-z A-Z = <>]','' , moons)
    moons = moons.split("\n")
    for pos in moons:
        pos = pos.split(",")
        moon_info.append(Moon(pos[0], pos[1], pos[2]))
    return moon_info

# class Vector2:
#     def __init__(self, x, y, z):
#         self.x = x
#         self.y = y
#         self.z = z

class Moon():
    def __init__(self, posx, posy, posz, vecx=0, vecy=0, vecz=0):
        self.posx = int(posx)
        self.posy = int(posy)
        self.posz = int(posz)
        self.vecx = int(vecx)
        self.vecy = int(vecy)
        self.vecz = int(vecz)
    
    def gravity(self, moon):
        #x
        if self.posx > moon.posx:
            self.vecx -= 1
            moon.vecx += 1
        elif self.posx < moon.posx:
            self.vecx += 1
            moon.vecx -= 1
        else:
            pass
        #y
        if self.posy > moon.posy:
            self.vecy -= 1
            moon.vecy += 1
        elif self.posy < moon.posy:
            self.vecy += 1
            moon.vecy -= 1
        else:
            pass
        #z
        if self.posz > moon.posz:
            self.vecz -= 1
            moon.vecz += 1
        elif self.posz < moon.posz:
            self.vecz += 1
            moon.vecz -= 1
        else:
            pass
        pass

    def apply_velocity(self):
        self.posx += self.vecx
        self.posy += self.vecy
        self.posz += self.vecz

        


def moon_energy(moons, step_num):
    interaction_ls = []
    steps = 0
    while steps < step_num:
        for moon1 in moons:
            for moon2 in moons:
                if moon1 == moon2:
                    continue
                elif [moon1, moon2] in interaction_ls or [moon2, moon1] in interaction_ls:
                    continue
                else:
                    moon1.gravity(moon2)
                    interaction_ls.append([moon1, moon2])
        for moon in moons:
            moon.apply_velocity()
        interaction_ls.clear()
        steps += 1 
    ans = [(abs(i.posx) + abs(i.posy) + abs(i.posz)) * (abs(i.vecx) + abs(i.vecy) + abs(i.vecz)) for i in moons]
    return sum(ans)

def match_state(moons):
    initial_state = [moons]
    final_state = []
    interaction_ls = []
    steps = 0
    run = True
    while run:
        for moon1 in moons:
            for moon2 in moons:
                if moon1 == moon2:
                    continue
                elif [moon1, moon2] in interaction_ls or [moon2, moon1] in interaction_ls:
                    continue
                else:
                    moon1.gravity(moon2)
                    interaction_ls.append([moon1, moon2])
        for moon in moons:
            moon.apply_velocity()
            final_state.append(moon)
        steps += 1
        print(steps)
        if initial_state == final_state:
            return steps
        final_state.clear()
        interaction_ls.clear()

if __name__ == "__main__":
    with open("inputday12.txt", "r") as f:
        f_read = f.read()
    input = moon_parse(f_read)
    print(moon_energy(input, 1000))
    # match_state(input)