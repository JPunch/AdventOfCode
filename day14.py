import re


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