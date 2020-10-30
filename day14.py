import re
import math
from collections import defaultdict


def fuel_parse(fuel_ls, storage):
    lines = re.sub(",", "", fuel_ls)
    lines = lines.split("\n")
    for line in lines:
        left, right = line.split("=>")
        storage.add_equation(Equation(left, right))

    return storage


class Equation:
    def __init__(self, left, right):
        self.product_value, self.product = self.parse_product(right)
        self.reactants, self.reactant_dict = self.parse_reactants(left)

    def parse_product(self, right):
        match = re.findall(r"\d+\s\w+", right)
        value, id = match[0].split()
        return int(value), id

    def parse_reactants(self, left):
        reactants, reactant_dict = [], {}
        matches = re.findall(r"\d+\s\w+", left)
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
        return f"Product {self.product_value} {self.product} => {self.reactant_dict.keys()}, {self.reactant_dict.values()}"


class Storage:
    def __init__(self):
        self.equations = []
        self.active_reactants = []
        self.reactant_needed = defaultdict()
        self.reactant_stored = defaultdict()

    def add_equation(self, equation):
        self.equations.append(equation)
        for reactant in equation.reactants:
            self.update_stored(reactant, 0)

    def update_stored(self, id, value):
        try:
            self.reactant_stored[id] += value
        except:
            self.reactant_stored[id] = value

    def update_needed(self, id, value):
        try:
            self.reactant_needed[id] += value
        except:
            self.reactant_needed[id] = value

    def check_stored(self, equation):
        amount_needed = self.reactant_needed[equation.product]
        amount_stored = self.reactant_stored[equation.product]
        difference = amount_stored - amount_needed

        if difference > 0:
            self.reactant_needed[equation.product] = 0
            self.reactant_stored[equation.product] = difference
        else:
            self.reactant_needed[equation.product] = 0
            made_per_reaction = equation.product_value
            scaler = math.ceil(abs(difference) / made_per_reaction)
            amount_stored = difference + (scaler * made_per_reaction)
            self.reactant_stored[equation.product] = amount_stored
            self.update_all(equation, scaler)

    def update_all(self, equation, scaler):
        reactant_dict = equation.reactant_dict
        for reactant in reactant_dict:
            self.update_needed(reactant, scaler * reactant_dict[reactant])

    def fuel_equation(self, equation):
        reactant_dict = equation.reactant_dict
        for reactant in reactant_dict:
            self.update_needed(reactant, reactant_dict[reactant])


def solver(storage):
    run = True
    for equation in storage.equations:
        if equation.product == "FUEL":
            storage.active_reactants.extend(equation.reactants)
            storage.fuel_equation(equation)
    while run == True:
        # find the equation round up and scale amount
        for equation in storage.equations:
            if equation.product in storage.active_reactants:
                storage.check_stored(equation)

                storage.active_reactants.remove(equation.product)
                storage.active_reactants.extend(equation.reactants)

        if len(storage.active_reactants) == storage.active_reactants.count("ORE"):
            # print("Finished")
            run = False

    return storage.reactant_needed["ORE"]


def solverp2(storage):
    count = 0
    run = True
    for equation in storage.equations:
        if equation.product == "FUEL":
            final_reaction = equation
            storage.active_reactants.extend(final_reaction.reactants)
            storage.fuel_equation(final_reaction)
    while run == True:
        # find the equation round up and scale amount
        for equation in storage.equations:
            if count == 1:
                scale_up = math.floor(999999000000 / storage.reactant_needed["ORE"])
                storage.reactant_needed["ORE"] = (
                    storage.reactant_needed["ORE"] * scale_up
                )
                for product in storage.reactant_stored:
                    storage.reactant_stored[product] = (
                        storage.reactant_stored[product] * scale_up
                    )
                count = scale_up
            elif equation.product in storage.active_reactants:
                storage.check_stored(equation)

                storage.active_reactants.remove(equation.product)
                storage.active_reactants.extend(equation.reactants)

        if storage.reactant_needed["ORE"] > 1000000000000:
            run = False

        elif len(storage.active_reactants) == storage.active_reactants.count("ORE"):
            count += 1
            print(f"ORE count: {storage.reactant_needed['ORE']}, FUEL count: {count}")
            storage.active_reactants.clear()
            storage.active_reactants.extend(final_reaction.reactants)
            storage.fuel_equation(final_reaction)

    return count


# ANSWER FOR THE EXAMPLE IS 31 ORE


if __name__ == "__main__":
    with open("inputday14.txt", "r") as f:
        lines = f.read()
    storage = Storage()
    fuel_ls = fuel_parse(lines, storage)
    # print(solver(fuel_ls))
    print(solverp2(fuel_ls))
    # 3919672 too high
