nombre_unicode = [69, 110, 122, 111, 32,                       #Enzo_
                  77, 111, 114, 97, 116, 97, 32,               #Morata_
                  65, 115, 116, 117, 100, 105, 108, 108, 111]  #Astudillo      

nombre = chr(32)  #_           
for char in map(chr, nombre_unicode):
    nombre += char
print(nombre)
