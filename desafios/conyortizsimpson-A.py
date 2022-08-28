print("Hoy sumaremos con manitos")
primer_numero = int(input("Ingresa el primer número a sumar: "))
segundo_numero = int(input("Ingresa el segundo número a sumar: "))

class Manos:
    def __init__(self):
        self.dedos = 10
        self.dedos_arriba = 0
        
    def subir_dedo(self):
        self.dedos_arriba += 1
        dedos_abajo = self.dedos - self.dedos_arriba
        # Traté de hacer un ascii pero el arte no es lo mío
        mano = "x"*self.dedos_arriba + "o"*dedos_abajo
        mano = "\t"+mano[:int(len(mano)/2)] + " " + mano[int(len(mano)/2):] + "\n"
        print(mano)
        if self.dedos_arriba == self.dedos:
            self.dedos_arriba = 0
            print("Completé una mano\n")
            return True
        return False
        
manitos = Manos()
manos = 0
dedos = 0

# Así sumo yo en mi cabeza, ya?
for i in range(primer_numero):
    nueva = manitos.subir_dedo()
    if nueva:
        manos += 1
for i in range(segundo_numero):
    nueva = manitos.subir_dedo()
    if nueva:
        manos += 1

dedos = manitos.dedos_arriba
total = manos * 10 + dedos
print(f"Como tengo {manos} manos llenas, \ny en las que no he completado {dedos} dedo(s), \nentonces la suma es de {total}")

print(f"\nSUMA: {total}")
