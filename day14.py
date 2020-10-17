import re

<<<<<<< HEAD
#
def fuel_parse(fuel_ls):
    '''
    Returns a dictionary with key of right hand side of the equation made into the element class
    and a key value of all the entries on the left hand side made into the element class
    '''
    fuel_dict = {}
=======

class Equation():
    def __init__(self, left, right):
        self.product_value, self.product = self.parse_product(right)
        self.reactants, self.reactant_dict = self.parse_reactants(left)

    def parse_product(self, right):
        match = re.findall("\d+\s\w+", right)
        return match[0].split()

    def parse_reactants(self, left):
        reactants, reactant_dict = [], {}
        matches = re.findall("\d+\s\w+", left)
        for match in matches:
            value, name = match.split()
            reactants.append(name)
            reactant_dict[name] = value
        return reactants, reactant_dict
    
    def __str__(self):
        return f"Product {self.product_value} {self.product} => {self.reactant_dict.keys(), self.reactant_dict.values()}"


class Storage():
    def __init__(self):
        self.equations = []
        self.simplify = []

    def add_equation(self, equation):
        self.equations.append(equation)

    def add_simplify(self, simplify):
        self.equations.append(simplify)


def fuel_parse(fuel_ls, storage):
>>>>>>> 87a928457e175a1e348dc65c6162746ca38cc4ab
    lines = re.sub(",", "", fuel_ls)
    lines = lines.split("\n")
    for line in lines:
        left, right = line.split("=>")
        storage.add_equation(Equation(left, right))        

    return storage


def simplify(equation):
    pass

def foobar(storage):
    run = True
<<<<<<< HEAD
    current_elements = []
    next_elements = []
    current_dict = ["1 FUEL"]
    while run == True:
        count = 1
        for element in current_dict:
            value, name = element.split()
            if name in fuel_ls.keys():
                next_elements.extend(fuel_ls[name]["reactants"])
        print(next_elements)
        print("\n")
        current_dict = next_elements[:]
        count ++ 1 
        if(len(next_elements) == 0):
            run = False   
        next_elements.clear()

            

class Reaction():
    def __init__(self, product, product_value, reactants):
        self.product = product
        self.product_value = product_value
        self.reactants = []
        self.reactant_values = []

    def parse_reactants(self, reactants):
        matchs = re.findall("(\d+\s\w+)", reactants)
        for match in matchs:
            self.reactants.extend(match.split()[0])
            self.reactant_values.extend(match.split()[1])
=======
    for equation in storage.equations:
        if equation.product == "FUEL":
            final_reaction = equation
    while run == True:

        for equation in storage.equations:
            if equation.product in final_reaction.reactants:
                final_reaction.reactants.remove(equation.product)
                final_reaction.reactants.extend(equation.reactants)
                # final_reaction.reactant_dict[equation.product] = equation.reactants
        
    return None #NOTHING

# ANSWER FOR THE EXAMPLE IS 165 ORE

>>>>>>> 87a928457e175a1e348dc65c6162746ca38cc4ab

#nect step is to regex match each number + reactant name combo to be used when creating a list to search for the next set of items
if __name__ == "__main__":
    with open("inputday14ex.txt", "r") as f:
        lines = f.read()
    # print(lines)
    storage = Storage()
    fuel_ls = fuel_parse(lines, storage)
    foobar(fuel_ls)
    # ore_count = calc_fuel(fuel_ls)
    # calc_fuel(fuel_ls)