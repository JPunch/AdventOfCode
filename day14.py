import re
from collections import defaultdict


class Equation:
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
            reactant_dict[name] = int(value)
        return reactants, reactant_dict

    def __str__(self):
        return f"Product {self.product_value} {self.product} => {self.reactant_dict.keys(), self.reactant_dict.values()}"


class Storage:
    def __init__(self):
        self.equations = []
        self.simplify = []
        self.current_reactants = []
        self.temp_dict = defaultdict()

    def add_equation(self, equation):
        self.equations.append(equation)

    def add_simplify(self, simplify):
        self.equations.append(simplify)

    def update_temp(self, id, value):
        if id in self.temp_dict:
            self.temp_dict[id] += value
        else:
            self.temp_dict[id] = value

    def update_all(self, equation):
        reactant_dict = equation.reactant_dict
        self.update_temp(equation.product, int(equation.product_value))
        for reactant in reactant_dict:
            self.update_temp(
                reactant,
                int(storage.temp_dict[reactant]) - int(reactant_dict[reactant]),
            )


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
            final_reaction = equation
            storage.current_reactants.extend(final_reaction.reactants)
    while run == True:

        for equation in storage.equations:
            if equation.product in storage.current_reactants:
                storage.update_all(equation)
                storage.current_reactants.remove(equation.product)
                storage.current_reactants.extend(equation.reactants)
                count += 1

        if len(final_reaction.reactants) == final_reaction.reactants.count("ORE"):
            run = False

    return print(count)


if __name__ == "__main__":
    with open("inputday14ex.txt", "r") as f:
        lines = f.read()

    storage = Storage()
    fuel_ls = fuel_parse(lines, storage)
    solver(fuel_ls)
