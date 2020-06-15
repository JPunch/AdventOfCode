import math


with open("C:/Users/crabb/OneDrive/Documents/VSC/AdventOfCode/inputday1.txt", "r")as f:
    f_read = f.read()
    fuel = f_read.split("\n")
    fuel = [int(i) for i in fuel]
    f.close()


def fuel4fuel(mass):
    fuelreq = math.floor(mass / 3) - 2
    fuelfinal = 0
    while fuelreq > 8:
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



fue = 0
suum = 0

def recur(f_list):
    global fue
    if len(f_list) == 0:
        print(fue)
    else:
        a = f_list.pop()
        fue += recur2(a)
        recur(f_list)

def recur2(f):
    global suum
    a = 0
    if f > 8:
        a = math.floor(f / 3) - 2
        suum += a
        return recur2(a)
    else:
        b = suum
        suum = 0
        return(b)

recur(fuel)