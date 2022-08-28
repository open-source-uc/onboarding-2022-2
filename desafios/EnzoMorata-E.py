from os import remove, path

archivo = open("EnzoMorata-E.py", "r")
lineas = archivo.readlines()
archivo.close()

path_archivo_actual = path.abspath(__file__)
nombre_archivo_actual = path.basename(__file__)

nombre_copia1 = nombre_archivo_actual.split(".")[0] + "(1).py"
nombre_copia2 = nombre_archivo_actual.split(".")[0] + "(2).py"

remove(path_archivo_actual)

copia1 = open(nombre_copia1, "w")
for i in lineas:
    print(i, end="", file=copia1)
copia1.close()

copia2 = open(nombre_copia2, "w")
for i in lineas:
    print(i, end="", file=copia2)
copia1.close()