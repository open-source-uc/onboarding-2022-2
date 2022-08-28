def phi(n, a=1, b=1):
    try:
        if n > 0:
            return(phi(n-1, b, a+b))
        else:
            return print(f"\u03C6 = {b/a}") #La razón aurea o phi se puede calcular como el lim_{n->inf} f(n+1)/f(n), con f algun numero de la sucesion de fibonacci
    except TypeError as error:
        print("Ingresa un numero válido")
    except RecursionError as error2:
        print("Ingresa una cantidad de recursión bajo 997")
print(phi(995))
# La máxima cantidad de recursiones (supuestamente) por defecto en python son 997
# No se porqué solo funciona desde 995 para abajo
# Esto se puede cambiar con sys.setrecursionlimit(numero)