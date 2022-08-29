import shutil
import os
import sys

ruta = sys.argv[0]

for i in range(2):
    copia = "MarcosSantelices-E{numero}.py".format(numero=i)
    nuevo_archivo = os.path.join("desafios", copia)
    shutil.copy(ruta, nuevo_archivo)

os.remove(ruta)
