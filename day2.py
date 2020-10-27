from copy import copy

with open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday2.txt", "r") as f:
    f_read = f.read()

intcode = f_read.split(",")
intcode= [int(i) for i in intcode]
print(intcode)

def Intcode(code, input1, input2):
    code[1], code[2] = input1, input2
    # run = True
    # i = 0
    # while run is True:
    for i in range(int(len(code)/4)):
        opcode = code[0 + 4 * i]
        parameter1, parameter2, parameter3 = code[1 + 4 * i], code[2 + 4 * i], code[3 + 4 * i]
        if opcode == 1:
            code[parameter3] = (code[parameter1] + code[parameter2])
            # i += 1
        elif opcode == 2:
            code[parameter3] = (code[parameter1] * code[parameter2])
            # i += 1
        elif opcode == 99:
            break
        else:
            print("Found an unknown opcode", code[opcode])
            break
    return code


def FindIntput(code):
    for input1 in range(100):
        for input2 in range(100):
            if Intcode(copy(code), input1, input2)[0] == 19690720:
                return input1, input2
           
i1, i2 = FindIntput(intcode)
print(100*i1 + i2)
#19690720