def multiplicacion_cursed(a:int, b:int):
    #Solo sirve para números enteros
    lista_contador1 = list()
    lista_contador2 = list()
    resultado = 0

    for i in range(a):
        lista_contador1.append(1)
    for j in range(b):
        lista_contador2.append(1)

    lista_final = lista_contador1*len(lista_contador2)

    for j in range(len(lista_final)):
        resultado += 1
        
    return resultado

a = multiplicacion_cursed(20, 5)
print(a)
