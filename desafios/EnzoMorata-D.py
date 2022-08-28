#saqué la idea de este video de quantum fracture: https://youtu.be/DQ5qqHukkAc
#calcular Pi por medio de poligonos regulares, el cálculo es bastante directo, 
# así que agregaré una forma de visualizar mediante prints cómo evolucionan los decimales mientras aumenta el n

#Considerando que el calculo de pi es el perimetro de una circunferecia dividido en su diametro, 
# buscaremos aproximarlo con un poligono regular de n lados. Si desde su centro tiramos rectas de largo r
#  a los vertices, los angulos alpha que se forman son igual a 360°/n. Luego, de los triangulos
#  por trigonometria podemos despejar que el lado(~arco) frente al angulo alpha mide 2rsen(alpha/2)
# el perimetro es igual a n*2rsen(alpha/2) y dividido en 2r, Pi≈n*sen(alpha/2) = n*sen(360°/2n)

from math import sin, radians
condicion = True
while condicion:
    condicion = False
    try:
        print("A continuación se calculará pi por aproximación de poligonos regulares. Deberás ingresar un número. *Con 57 se aproxima hasta el segundo decimal (3,14...).")
        n = int(input("Ingresa un n (int), para la cantidad de iteraciones(prints) que se mostrarán. Cuidado con el número, prueba un pequeño primero\n"))
    except ValueError as error:
        print("utiliza un número válido")
        condicion = True 

for i in range(1, n + 1):
    pi = i * sin(radians(360)/(2*i))
    print(f"N = {i}: Pi ≈ {pi}")
