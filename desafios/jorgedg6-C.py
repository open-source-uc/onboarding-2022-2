from time import sleep

#Definimos la base (Crucial) Prueba cambiandola.. (Peligro!)
base = 69
#Definimos el codigo secreto
#Generado con función en jorgedg6-C.py:74
codigo = [5, 10, 13, 2, 0]
#Imprimimos la introducción
#Generada con función en jorgedg6-C.py:53
print(chr(base + 3) + chr(base + 42) + chr(base + 39)\
	 + chr(base + 28) + chr(base - 36) + chr(base - 37)\
		 + chr(base + 3) + chr(base + 42) + chr(base + 52)\
			 + chr(base - 37) + chr(base + 36) + chr(base + 40)\
				 + chr(base + 43) + chr(base + 45) + chr(base + 36)\
					 + chr(base + 40) + chr(base + 36) + chr(base + 45)\
						 + chr(base + 164) + chr(base - 37) + chr(base + 40)\
							 + chr(base + 36) + chr(base - 37) + chr(base + 41)\
								 + chr(base + 42) + chr(base + 40) + chr(base + 29)\
									 + chr(base + 45) + chr(base + 32) + chr(base - 37)\
										 + chr(base + 46) + chr(base + 36) + chr(base + 41)\
											 + chr(base - 37) + chr(base + 48) + chr(base + 46)\
												 + chr(base + 28) + chr(base + 45) + chr(base - 37)\
													 + chr(base + 30) + chr(base + 42) + chr(base + 40)\
														 + chr(base + 36) + chr(base + 39) + chr(base + 39)\
															 + chr(base + 28) + chr(base + 46) + chr(base - 36))
for i in range(15):
	#sleep(0.5)
	print(chr(base - 37))
	if i == 3:
		print(chr(base - 3) + chr(base + 48) + chr(base + 32)\
			 + chr(base + 41) + chr(base + 28) + chr(base - 37)\
				 + chr(base + 47) + chr(base + 164) + chr(base + 30)\
					 + chr(base + 41) + chr(base + 36) + chr(base + 30)\
						 + chr(base + 28) + chr(base - 37) + chr(base + 31)\
							 + chr(base + 36) + chr(base + 45) + chr(base + 168)\
								 + chr(base + 28) + chr(base - 37) + chr(base + 52)\
									 + chr(base + 42))
#Desciframos el código de nombre
i = 0
for num in codigo:
	codigo[i] = chr(base + num)
	i += 1
del i
#Demostramos superioridad
print(chr(base - 27)*10 + chr(base - 37) + chr(base - base).join(codigo)\
	 + chr(base - 37) + chr(base - 27)*10)
print(chr(base - 37))


###############################
#        NO EJECUTADO         #
###############################
#Funcion de Conversión
#Transformacion a comando
def convertir(frase, base):
	comando_final = ""
	for letra in frase:
		if ord(letra) < base:
			comando_final += f"chr(base - {abs(base - ord(letra))}) + "
		else:
			comando_final += f"chr(base + {abs(base - ord(letra))}) + "
	return comando_final[:-2]
#Guardado de comando
#x = convertir("Hola! Hoy imprimiré mi nombre sin usar comillas!", base)
#y = convertir("Buena técnica diría yo", base)
#Printeo del comando
#print(x)
#print(y)
#Evaluación automatica comando
#print(eval(x))
#print(eval(y))

#Funcion de Codigo
#Creacion de codigo
def generar_codigo(frase, base):
	codigo = []
	for letra in frase:
		if ord(letra) < base:
			codigo.append(ord(letra) - base)
		else:
			codigo.append(base - ord(letra))
	return codigo