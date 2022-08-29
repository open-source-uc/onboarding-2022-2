num_a = int(input("Ingrese primer numero: "))
num_b = int(input("Ingrese segundo numero: "))

suma_multiplicacion = []
multiplicaion = 0

for i in range(num_a):
    aux = []
    for j in range(num_b):
        aux.append(1)
    suma_multiplicacion.append(aux)

for lista in suma_multiplicacion:
    multiplicaion += sum(lista)

print(f"El resultado de la multiplicacion(?) es: {multiplicaion}")
