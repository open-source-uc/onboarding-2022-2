texto = open("cadaeic_cadenza.txt",'r')
cc = [] #Lista de listas de palabras por linea
#Limpieza
for linea in texto.readlines():
    linea = linea.strip('():-.,?!" \n')
    #lineas vacías no sirven
    if linea != '':
        linea = linea.split()
        lineadef = [] #lista de palabras con la menor cantidad de caracteres "no letra" posible
        for palabra in linea:
            palabra = palabra.strip('():-.,?!" \n')
            #palabras vacías no sirven
            if palabra != '':
                #considerando que en el texto hay palabras unidas por "..." o "-"
                if '...' in palabra:
                    palabras = palabra.split('...')
                    for palabradef in palabras:
                        lineadef.append(palabradef)
                elif '-' in palabra:
                    palabras = palabra.split('-')
                    for palabradef in palabras:
                        lineadef.append(palabradef)
                else:
                    lineadef.append(palabra)
        cc.append(lineadef)
texto.close()
digitos = [] #Lista de dígitos de pi
for linea in cc:
    for palabra in linea:
        digito = 0
        for caracter in palabra:
            if caracter.lower() in "abcdefghijklmnopqrstuvwxyz":
                digito += 1
        if digito > 0:
            if digito == 10:
                digito = 0
            digitos.append(str(digito))
pi = ''
pi += digitos[0] + '.'
for decimal in digitos[1:len(digitos)]:
    pi += decimal
print("Pi = " + pi)
print(float(pi))

#Por si no se puede subir el archivo de texto, este era: http://www.cadaeic.net/cadenza.htm