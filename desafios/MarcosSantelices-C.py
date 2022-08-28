x = input()
string_inicial = str(x)
lista = []
string_final = str()

for i in string_inicial:
    numero = ord(i)
    lista.append(numero)

for j in lista:
    string_final += chr(j)

print(string_final)
