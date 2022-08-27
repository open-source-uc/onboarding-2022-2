import os
import shutil


def mitosis():
    lista_archivos = os.listdir('desafios')

    if 'isufan-E.py' in lista_archivos:
        shutil.copy(__file__, 'desafios/isufan-E-copia_1.py')
        shutil.copy(__file__, 'desafios/isufan-E-copia_2.py')
    else:
        copia_mayor = 2
        for archivo in os.listdir('desafios'):
            if 'isufan-E-copia' in archivo:
                n_copia = int(archivo.strip('.py').split('_')[1])
                if n_copia > copia_mayor:
                    copia_mayor = n_copia
        shutil.copy(__file__, f'desafios/isufan-E-copia_{copia_mayor + 1}.py')
        shutil.copy(__file__, f'desafios/isufan-E-copia_{copia_mayor + 2}.py')

    os.remove(__file__)


mitosis()
