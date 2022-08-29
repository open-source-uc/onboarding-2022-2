from random import randint
from math import pi

radius = int(input("Radio (número entero): "))
iterations = int(input("Iteraciones: "))

canvas = [[""]*radius for x in range(radius)]
for x in range(radius):
    for y in range(radius):
        if x**2 + y**2 <= radius**2 + 0.0001:
            canvas[x][y] = True
        else:
            canvas[x][y] = False

acc = 0
for i in range(iterations):
    x = randint(0, radius-1)
    y = randint(0, radius-1)
    if canvas[x][y]:
        acc += 1

probability = acc / iterations
error = abs(4*probability - pi)

print(f"Probabilidad: {round(100*probability)}%")
print(f"Resultado: {4*probability}")
print(f"Error: {round(100*error/pi)}% ({error})")
