from math import sqrt, log10, log, exp, fabs, copysign, sin, cos, pi


def pedir_numeros():
    n1_ingresado = False
    n2_ingresado = False
    while not n1_ingresado:
        try:
            n1 = float(input(('Ingresa el primer número: ')))
        except ValueError:
            print('Ingresa un primer número válido.')
        else:
            n1_ingresado = True
    while not n2_ingresado:
        try:
            n2 = float(input(('Ingresa el segundo número: ')))
        except ValueError:
            print('Ingresa un segundo número válido.')
        else:
            n2_ingresado = True
    return [n1, n2]


numeros = pedir_numeros()
print(f'Resultado suma: {round(copysign(sqrt(((cos(pi)**2)*(copysign(fabs(exp(log(log10(10**sqrt(sum(numeros)**2))))), exp(log(log10(10**sqrt(sum(numeros)**2))))))**2) + ((sin(pi)**2)*(copysign(fabs(exp(log(log10(10**sqrt(sum(numeros)**2))))), exp(log(log10(10**sqrt(sum(numeros)**2))))))**2)), sum(numeros)), 3)}')
# Sólo un poquito más ineficiente que hacer sum(numeros)
