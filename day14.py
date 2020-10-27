import re
from collections import defaultdict


class Equation:
    def __init__(self, left, right):
        self.product_value, self.product = self.parse_product(right)
        self.reactants, self.reactant_dict = self.parse_reactants(left)

    def parse_product(self, right):
        match = re.findall("\d+\s\w+", right)
        value, id = match[0].split()
        return int(value), id

    def parse_reactants(self, left):
        reactants, reactant_dict = [], {}
        matches = re.findall("\d+\s\w+", left)
        for match in matches:
            value, name = match.split()
            reactants.append(name)
            reactant_dict[name] = int(value)
        return reactants, reactant_dict

    def update_dict(self, id, value):
        if id in self.reactant_dict:
            self.reactant_dict[id] += int(value)
        else:
            self.reactant_dict[id] = int(value)

    def __str__(self):
        return f"Product {self.product_value} {self.product} => {self.reactant_dict.keys(), self.reactant_dict.values()}"


class Storage:
    def __init__(self):
        self.equations = []
        self.active_reactants = []
        self.reactant_needed = defaultdict()
        self.reactant_stored = defaultdict()

    def add_equation(self, equation):
        self.equations.append(equation)

    def update_temp(self, id, value):
        if id in self.reactant_stored:
            self.reactant_stored[id] += value
        else:
            self.reactant_stored[id] = value

    def update_all(self, equation):
        amount_needed = self.reactant_needed[equation.product]
        amount_stored = storage.reactant_stored[equation.product]
        reactant_dict = equation.reactant_dict
        for reactant in reactant_dict:
            self.update_temp(reactant, reactant_dict[reactant])


def fuel_parse(fuel_ls, storage):
    lines = re.sub(",", "", fuel_ls)
    lines = lines.split("\n")
    for line in lines:
        left, right = line.split("=>")
        storage.add_equation(Equation(left, right))

    return storage


def solver(storage):
    run = True
    count = 0
    for equation in storage.equations:
        if equation.product == "FUEL":
            storage.active_reactants.extend(equation.reactants)
            storage.update_all(equation)
    while run == True:
        # find the equation round up and scale amount
        for equation in storage.equations:
            if equation.product in storage.active_reactants:
                storage.update_all(equation)

                storage.active_reactants.remove(equation.product)
                storage.active_reactants.extend(equation.reactants)

        if len(storage.active_reactants) == storage.active_reactants.count("ORE"):
            # print("Finished")
            run = False

    return print(count)


# I need a check to see if a dictionary entry already exists and then if it exists reevaluate the amount of the next product for the new amount and then update and those new ones are checked also
# ANSWER FOR THE EXAMPLE IS 31 ORE


# nect step is to regex match each number + reactant name combo to be used when creating a list to search for the next set of items
if __name__ == "__main__":
    with open("inputday14ex.txt", "r") as f:
        lines = f.read()
    # print(lines)
    storage = Storage()
    fuel_ls = fuel_parse(lines, storage)
    solver(fuel_ls)
    # ore_count = calc_fuel(fuel_ls)
    # calc_fuel(fuel_ls)