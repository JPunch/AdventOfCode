f = open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday2.txt", "r")
f_read = f.read()
intcode = f_read.split(",")
#fuel.pop()
intcode= [int(i) for i in intcode]
f.close()
print(intcode)

def Intcode(code):
    code[1], code[2] = 12, 2
    print(code)
    run = True
    i = 0
    while run is True:
        a = code[0 + 4 * i]
        print(a)
        if a == 1:
            b, c, d = code[1 + 4 * i], code[2 + 4 * i], code[3 + 4 * i]
            code[d] = (code[b] + code[c])
            i += 1
            continue
        if a == 2:
            b, c, d = code[1 + 4 * i], code[2 + 4 * i], code[3 + 4 * i]
            code[d] = (code[b] * code[c])
            i += 1
            continue
        if a == 99:
            run = False
        else:
            print("Found an unknown opcode", code[a])
            run = False
    print(code)

Intcode(intcode)