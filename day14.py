import re


class element:
    def __init__(self, ele):
        self.amount = int(ele.split()[0])
        self.name = ele.split()[1]


def fuel_parse(fuel_ls):
    '''
    Returns a dictionary with key of right hand side of the equation made into the element class
    and a key value of all the entries on the left hand side made into the element class
    '''
    fuel_dict = {}
    for line in fuel_ls:
        left, right = line.split("=>")
        right = element(right)
        left = left.split(",")
        left = [element(item) for item in left]
        fuel_dict[right] = left
    return fuel_dict

def calc_fuel(fuel_ls):
    run = True
    current_elements = []
    next_elements = []
    current_dict = ["FUEL"]
    while run == True:
        for item in fuel_ls.keys:
            if len(current_dict) == current_dict.count("ORE"):
                run = False
            elif item.name in current_dict:
                next_elements.append(item[item.name])
        for item in next_elements:
            pass
            
        


if __name__ == "__main__":
    with open("inputday14.txt", "r") as f:
        lines = f.readlines()
    # print(lines)
    
    fuel_ls = fuel_parse(lines)
    # ore_count = calc_fuel(fuel_ls)
    print(fuel_ls)