"""
Desafío E: Hacer un programa que haga mitosis.
Es decir, que cada vez que se corra se elimine y a la vez se creen 2 copias.
"""
import os

madre = __file__

archivo = open(madre, 'r')
codigo_mitosis = archivo.read()
archivo.close()

nombre = os.path.basename(madre)[:-3]

for i in range(1, 3):
	hija = open(f"{nombre} ({i}).py", "w+")
	hija.write(codigo_mitosis)
	hija.close()

os.remove(__file__)
