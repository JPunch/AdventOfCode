import re


def fuel_parse(fuel_ls):
    '''
    Returns a dictionary with key of right hand side of the equation made into the element class
    and a key value of all the entries on the left hand side made into the element class
    '''
    fuel_dict = {}
    lines = re.sub(",", "", fuel_ls)
    lines = lines.split("\n")
    for line in lines:
        matches = re.match("(\d+\s\w+)", line)
        print(matches)
        left, right = line.split("=>")
        reactants = left.split()
        value, product = right.split()
        fuel_dict[product] = {"value": value, "reactants": reactants}
    return fuel_dict

def calc_fuel(fuel_ls):
    run = True
    current_elements = []
    next_elements = []
    current_dict = ["FUEL"]
    while run == True:
        count = 1
        for item in fuel_ls.keys():
            for element in current_dict:
                if(element in item and element not in "FUEL"):
                    next_elements.extend(fuel_ls[item])
        print(next_elements)
        print("\n")
        current_dict = next_elements
        next_elements.clear()
        count ++ 1
        if(len(next_elements) == 0):
            run = False    
            
        

#nect step is to regex match each number + reactant name combo to be used when creating a list to search for the next set of items
if __name__ == "__main__":
    with open("inputday14.txt", "r") as f:
        lines = f.read()
    # print(lines)
    
    fuel_ls = fuel_parse(lines)
    # ore_count = calc_fuel(fuel_ls)
    calc_fuel(fuel_ls)