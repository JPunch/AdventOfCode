'''Advent of Code 2019 day5'''

from copy import copy

with open("inputday2.txt", "r") as f:
    f_read = f.read()

intcode = f_read.split(",")
intcode = [int(i) for i in intcode]

def intcode(code, input1, input2):
    code[1], code[2] = input1, input2
    for i in range(int(len(code)/4)):
        opcode = getopcode(code[0 + 4 * i])
        modes = 
        parameter1, parameter2, parameter3 = code[1 + 4 * i], code[2 + 4 * i], code[3 + 4 * i]
        if opcode == 1:
            code[parameter3] = (code[parameter1] + code[parameter2])
            # i += 1
        elif opcode == 2:
            code[parameter3] = (code[parameter1] * code[parameter2])
            # i += 1
        elif opcode == 3:
            code[parameter3] = code[parameter1] + code[parameter2]
        elif opcode == 4:
            code[parameter3] = code[parameter1] + code[parameter2]
        elif opcode == 99:
            break
        else:
            print("Found an unknown opcode", code[opcode])
            break
    return code


def findinput(code):
    for input1 in range(100):
        for input2 in range(100):
            if intcode(copy(code), input1, input2)[0] == 19690720:
                return input1, input2

def modes(opcode):
    modes = opcode[:-2][::-1] #First 3 components and then reversed
    return modes

def getopcode(opcode):
    opcode = modes = opcode[-2:]
    return opcode
    
           
i1, i2 = findinput(intcode)
