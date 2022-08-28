print("Bienvenid@ a la suma de números enteros cursed\n\n")
condicion = True
while condicion:
    condicion = False
    try:
        num1 = int(input("Primer número\n"))
        num2 = int(input("Segundo número\n"))
    except ValueError as error:
        print("Ingresa un número válido")
        condicion = True    

digitos_cursed = []
for i in range(0, 10):
    digito_cursed = "" + "*"*i
    digitos_cursed.append(digito_cursed)

num1_cursed = ""
for i in range(0, len(str(num1))):
    digito = str(num1)[len(str(num1)) - i - 1]
    digito_cursed = digitos_cursed[int(digito)] * 10**i
    num1_cursed += digito_cursed

num2_cursed = ""
for i in range(0, len(str(num2))):
    digito = str(num2)[len(str(num2)) - i - 1]
    digito_cursed = digitos_cursed[int(digito)] * 10**i
    num2_cursed += digito_cursed

suma = num1_cursed + num2_cursed
stack = len(suma)//10
diferencia = len(suma)%10
for i in range(0, stack):
    print("*"*10)
print("*" * diferencia)
contador = 0
for i in suma:
    contador += 1
print(f"El resultado de la suma es {len(suma)}")

