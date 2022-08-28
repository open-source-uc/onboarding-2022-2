import os
import shutil
ruta = os.path.dirname(os.path.realpath(__file__))
for i in range(1, 3):
    shutil.copy('jeanPhilipe-E.py', os.path.join(ruta, f"copia{i}"))
os.remove(ruta)