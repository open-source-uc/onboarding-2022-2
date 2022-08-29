# Saqué la inspiración de un video de Joma Tech que había visto hace un tiempo (acerca de su "pregunta favorita de entrevistas", bien recomendado btw)
# Link al video: https://www.youtube.com/watch?v=pvimAM_SLic

# El método se llama Monte Carlo method, donde se inscribe una circunferencia en un cuadrado.
# Se colocan muchos puntos aleatoriamente dentro del área del cuadrado y se cuentan la cantidad de puntos dentro de la circunferencia y los puntos totales.
# El estimado de Pi es Pi = 4 * (puntos en circunferencia) / (puntos totales)

# Volví a ver el video cuando mi código ya lo tenía listo.
# El método es bien intuitivo de codificar, por eso que mi código puede parecerse al de Joma pero prometo que mi código es original.


from random import random
from math import sqrt


def pitagoras(c1, c2):
    return sqrt(c1**2 + c2**2)


def pi():
    puntos_dentro_circ = 0
    puntos_totales = 0
    for i in range(1000000):
        x = random()
        y = random()
        if pitagoras(x, y) < 1:
            puntos_dentro_circ += 1
        puntos_totales += 1

    pi = (4*puntos_dentro_circ)/puntos_totales
    return pi


print(pi())
