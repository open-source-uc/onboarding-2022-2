a = [67, 111, 110, 115, 116, 97, 110, 122, 97, 32, 79, 114, 116, 105, 122, 32, 83, 105, 109, 112, 115, 111, 110]
lista = []
for i in a:
    lista.append(chr(i))
nombre = lista[0]
for i in range(1, len(lista)):
    nombre += lista[i]
print(nombre)
