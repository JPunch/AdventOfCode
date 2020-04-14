import math


f = open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday1.txt", "r")
f_read = f.read()
fuel = f_read.split("\n")
fuel.pop()
fuel = [int(i) for i in fuel]
f.close()


def fuel4fuel(mass):
    fuelreq = math.floor(mass / 3) - 2
    fuelfinal = 0
    while fuelreq > 6:
        fuelfinal += fuelreq
#        print(fuelfinal)
        fuelreq = math.floor(fuelreq / 3) - 2
#        print(fuelreq)
        continue
    else:
        return(fuelfinal + fuelreq)

def fuel_counter_upper(f_list):
    fuelreq_ls = []
    for i in f_list:
        fuelreq = fuel4fuel(i)
        fuelreq_ls.append(fuelreq)
        totalf = sum(fuelreq_ls)
    print(totalf)

fuel_counter_upper(fuel)