from base64 import encode
import base64


nombre = '01000011 01110010 01101001 01110011 01110100 01101111 01100010 01100001 01101100 00100000 01010100 01101111 01110010 01110010 01100101 01110011 00100000 01000011 01100001 01110010 01110010 01100001 01110011 01100011 01101111'
nombre_binario = nombre.split()
nombre_string = ""

for letra_binario in nombre_binario:
    entero = int(letra_binario, 2)
    letra_ascii = chr(entero)
    nombre_string += letra_ascii

print(nombre_string)
