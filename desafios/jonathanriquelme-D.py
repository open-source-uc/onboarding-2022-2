# DESAFIO D DE ONBOARDING OSUC 2022-2
# Hecho por Jonathan Riquelme

# Cálculo de PI mediante el método MONTECARLO


from random import uniform
import numpy as np


# Función distancia

def dist(P):
    '''Distancia euclidiana entre origen y el punto P'''
    
    return np.sqrt(P[0]**2 + P[1]**2)

# Se define un cuadrado de lado X  que tiene un círculo dentro cuyo radio es X
# El centro de ambas figuras se encuentra en el origen

X = 10
N_circle, N_square = 0, 0   # cantidad inicial de colisiones


# Número de iteraciones (mientras más alta, más preciso será el pi estimado)
I = 10000000 # may take a while, but it's worth it
for _ in range(I):
    P = np.array([uniform(-X/2, X/2), uniform(-X/2, X/2)])

    if dist(P) < X/2: N_circle += 1

    N_square += 1


ratio = N_circle / N_square

pi_estimado = 4 * ratio

print(pi_estimado)
