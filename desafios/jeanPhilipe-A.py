import sympy
sympy.init_printing(use_unicode=True)

def operacion(numero1, numero2, opcion):
    if opcion == "sum":
        x, y = sympy.symbols('x y')
        f = (x**2-y**2)/(2*x-2*y)
        integral = sympy.integrate(f, x)
        derivada = sympy.diff(integral, x)
        print(2*derivada.subs(x, numero1).subs(y, numero2))
    elif opcion == "mul":
        x, y = sympy.symbols('x y')
        f = ((x + y)**2 - x**2 - y**2)/2
        integral = sympy.integrate(f, x)
        derivada = sympy.diff(integral, x)
        print(derivada.subs(x, numero1).subs(y, numero2))
    else:
        print("ingrese una opcion valida, [sum] para sumar y [mul] para multiplicar")


operacion(-1, 3, "sum")
operacion(-1, 3, "mul")