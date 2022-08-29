def multiplicar(num_a, num_b):
    if num_a < 0:
        a = num_a * -1
    else:
        a = num_a
    if num_b < 0:
        b = num_b * -1
    else:
        b = num_b

    resultado = 0
    for a1 in range(a):
        for b1 in range(b):
            resultado += 1
    if num_a < 0:
        if num_b >= 0:
            return resultado*-1
    else:
        if num_b < 0:
            return resultado*-1
    return resultado

num_a = int(input('ingrece un numero'))
num_b = int(input('ingrece otro numero'))

print(multiplicar(num_a, num_b))
