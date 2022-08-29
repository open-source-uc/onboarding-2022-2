def suma(a, b):
    numero_1 = 0
    for i in range(a):
        numero_1 += 1
        numero_1_nuevo = 0
        while numero_1_nuevo < numero_1:
            numero_1_nuevo += 1

        if numero_1_nuevo == numero_1:
            primer_numero = numero_1_nuevo
        else:
            primer_numero = numero_1

    numero_2 = 0
    for i in range(b):
        numero_2 += 1
        numero_2_nuevo = 0
        while numero_2_nuevo < numero_2:
            numero_2_nuevo += 1

        if numero_2_nuevo == numero_2:
            segundo_numero = numero_2_nuevo
        else:
            segundo_numero = numero_2

    suma_final = 0

    for i in range(numero_1):
        for j in range(numero_2):
            suma_final += 1

    return suma_final

a = int(input('numero 1:'))
b = int(input('numero 2:'))
print(suma(a, b))

# Lo siento, se que pudo ser mas largo pero no tuve mucho tiempoe esta semana :c
