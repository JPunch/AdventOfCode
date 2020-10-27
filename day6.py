with open("inputday6.txt", "r") as f:
    f_read = f.read()
orbit_ls = f_read.split("\n")
orbit_ls = [x.split(")") for x in orbit_ls] # list of two element lists same oreintation as before
# print(orbit_ls) #maybe make a set
# function that parses through that essentially counts how many steps away from com the point is therefore when you add something to the right of it the added orbit count is just that number from a dict
#look for com first and then for next element each time with an interger count adds orbits equal to count each time

def countorbits(orbit_ls):
    orbits = orbit_ls.copy()
    planet_tree = {}
    for orbit in orbits:
            if orbit[0] == "COM":
                planet_tree[orbit[1]] = 1
                orbits.remove(orbit)
    while len(orbits) > 0:
        for orbit in orbits:
            if orbit[0] in planet_tree:
                planet_tree[orbit[1]] = planet_tree[orbit[0]] + 1
                orbits.remove(orbit)
    return sum(planet_tree.values()), planet_tree

def tosanta(orbit_ls):
    orbits = orbit_ls.copy()
    planet_tree = countorbits(orbit_ls)[1]
    path = []
    for orbit in orbits:
            if orbit[1] == "YOU":
                currentplanet = orbit[0]
                path.append(currentplanet)
                orbits.remove(orbit)
    while currentplanet != "COM":
        for orbit in orbits:
            if currentplanet == orbit[1]:
                currentplanet = orbit[0]
                path.append(currentplanet)
                orbits.remove(orbit)
    for orbit in orbits:
            if orbit[1] == "SAN":
                currentplanet = orbit[0]
                orbits.remove(orbit)
    while currentplanet not in path:
        for orbit in orbits:
            if currentplanet == orbit[1]:
                currentplanet = orbit[0]
                orbits.remove(orbit)
    you = path.index(currentplanet)
    santa = planet_tree["SAN"] - planet_tree[currentplanet] - 1
    return you + santa


if __name__ == "__main__":
    # print(countorbits(orbit_ls))
    # print(tosanta(orbit_ls))
        
                


            
            
