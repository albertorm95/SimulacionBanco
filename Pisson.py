import math
import random

E=2.718
lamd=float(raw_input("Numero de veces que se espera que ocurra el fenomeno: "))
x=float(raw_input("Numero de ocurrencias del evento: "))

def poisson(lamd,x):
    poi=pow(lamd,x)*pow(E,-lamd)/math.factorial(x)
    print poi
    return poi
print 60*poisson(lamd,x)

