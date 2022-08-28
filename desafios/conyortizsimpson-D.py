# Gregory-Leibniz porque lo vi en un video y no se me ocurre otra forma

# En resumen, la sumatoria de n=0 al infinito de:
# (sumatoria) (-1)^n / 2n + 1 = pi/4

# Ahora busquemos pi ewe

fin = 1000000 # muy grande pero supongamos que es infinito
sumatoria = 0
for i in range(0, fin):
    arriba = (-1)**i
    abajo = 2*i+1
    sumatoria += arriba/abajo

pi = sumatoria * 4

print("Pi es:")
print(pi)

# Ojalá no tener que usar sumatorias de nuevo, un gustazo
