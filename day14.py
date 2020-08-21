import re

def fuel_parse(fuel_ls):
    fuel_dict = {}
    for line in fuel_ls:
        left, right = line.split("=>")
        right =re.sub(" ", "", right)
        left = left.split(",")

        fuel_dict[right] = left
    return fuel_dict

def calc_fuel(fuel_ls):
    return null

if __name__ == "__main__":
    with open("inputday14.txt", "r") as f:
        lines = f.readlines()
    print(lines)
    
    fuel_ls = fuel_parse(lines)
    # ore_count = calc_fuel(fuel_ls)
    print(fuel_ls)