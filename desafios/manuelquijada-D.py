# en resumen esto lo vi en un tiktok y no me acuerdo de quien era

import math

i = 1
term1 = math.sqrt(6)
term2 = 0

n = int(input("Numero entero positivo de gran magnitud: "))

while (i < n):
    term2 = term2 + ((1/i)**2)
    i = i + 1

pi = term1*(math.sqrt(term2))
print("PI =",pi)
