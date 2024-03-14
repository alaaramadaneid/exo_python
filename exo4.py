#Calcul de l'aire d'un cercle
import math

r = float(input("entrez R : "))

def Area(x):
    return math.pi * x **2
print("l'aire de cercle est : ",Area(r))