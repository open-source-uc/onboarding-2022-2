print("Esta es la forma más fácil existe para sumar")

input_incorrecto = True

while input_incorrecto:
    input_incorrecto = False

    try:
        a = int(input("Por favor ingresa el primer numero: "))
        b = int(input("Ahora, ingresa el segundo numero: "))
    
    except ValueError as eeeeeeee:
        print("Ingresaste otra cosa :| POR FAVOR INGRESA NUMEROS! :D")
        input_incorrecto = True

sumador_1 = []
sumador_2 = []

for i in range(a):
    sumador_1.append("ja")

for j in range(b):
    sumador_2.append("bruh")

def casi_olvido_uno(jordan23):
    lista_rectificadora = []

    for i in range(len(jordan23)):
        lista_rectificadora.append(i)
    
    lista_rectificadora.sort(reverse=True)

    chipetia = lista_rectificadora.pop(0) + 1
    
    print(f"si sako la {chipetia} los pongo a correr")

    return chipetia


def suma_suma(el, jordan23):
    resultado_final = 0
    lista_aseguradora_de_resultado = []
    if len(el) != 0:
        for i in range(len(el)):
            lista_aseguradora_de_resultado.append(i)
        for k in range(len(lista_aseguradora_de_resultado)):
            resultado_final += 1
    else:
        print("saque la 40")
            
    suman2 = casi_olvido_uno(jordan23)

    print("hello world") # ?



    for i in range(suman2):
        resultado_final += 2
    
    for k in range(suman2):
        resultado_final -= 1
    
    return resultado_final


algo = suma_suma(sumador_1, sumador_2)

print(f"Al final de cuentas me dio {algo}")





