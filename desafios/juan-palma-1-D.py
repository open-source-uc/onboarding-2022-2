#Aquí calcularemos el número 𝝋(Phi) o Aureo, conocido también como Razon de Oro o Divina:
#Este número puede ser encontrado/calculado de distintas maneras

#Primera Manera: Con Fibonacci

def fibonacci(n):
  if n <= 1:
    return 1
  return fibonacci(n-2) + fibonacci(n-1)

#Segunda Manera: Sin Fibonacci
# Esta manera me está costando un poco la voy a dejar para despues, era facil me enrredé solo 🤓
def numero_dorado(n):
  if n<=1:
    return 1
  return 1 + 1/numero_dorado(n-1) 

if __name__ == '__main__':

  #Aqui hacemos una cascada que nos muestra como va mejorando nuestro calculo a medida que vamos iterando

    number = int(input("Escoge un natural menor a 40 (o muere el pc 😂): "))
    texto_con_fibo = 'Con Fibonnaci (División de Términos)'
    texto_sin_fibo = 'Sin Fibonacci (Suma de Fracciones)'

    print(texto_con_fibo)
    for i in range(number):
      print(f'Iteración: N°{i+1}: {fibonacci(i+1) / fibonacci(i)}')

    print('\n')

    print(texto_sin_fibo)
    for i in range(number):
      print(f'Iteración: N°{i+1}: {numero_dorado(i+1)}')

    print('\n Mientras más itramos mejor es la aproximación')

  # Pregunta: ¿Que función aproxima mejor el número?