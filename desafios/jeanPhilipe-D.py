from asyncio.windows_events import INFINITE
import sympy
x = sympy.Symbol('x')
e = sympy.limit((1 + 1/x)**x, x, sympy.oo)
print(e)