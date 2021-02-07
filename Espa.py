from random import *
import os

verbes = open("verbes.txt","r")
temps = open("temps.txt","r")
r = verbes.readlines()
tps = temps.readlines()

nbv = int(input("Nombre de verbes: "))
os.system("cls")
for i in range(nbv):
    pick = r.pop(randint(0,len(r)-1))
    pick = pick[0:len(pick)-1]
    tpps = tps[randint(0,len(tps)-1)]
    print(str(pick) + " " + str(tpps),end="")
