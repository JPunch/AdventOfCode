from pair_programming.intcode import Memory, compute
from itertools import permutations
import subprocess


def max_thrust_input():
    combs = list(permutations([0, 1, 2, 3, 4], 5))  # list of tuples of combinations
    thrusts = []
    while len(combs) > 0:
        thrusts.append(get_thrust(combs.pop()))
    return None


def get_thrust(comb, memory):
    with open("inputday7.txt", "r") as in_file:
        program = in_file.read()
    mem = Memory(program)
    i = 0
    if i == 0:
        output = subprocess.run(compute(program), input=0)
        i += 1
    return None


if __name__ == "__main__":
    print(get_thrust)