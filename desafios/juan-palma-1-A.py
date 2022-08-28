# Definimos nuestra función espectaculars
def suma_dificil(first_number, second_number):
  total = 0
  tupla = [first_number, second_number]
  tupla.sort()

  # Obtenemos el primer dígito del número más grande
  digitos = str(tupla[1])
  digitos_int = int(len(digitos))
  
# La idea ahora es crear el loop menos óptimo posible (repitiendo código inecesariamente)
  for i in range(digitos_int):

    if tupla[0] // (10 ** i) != 0 and tupla[1] // (10 ** i) != 0:

      primer_componente = tupla[1] % 10 ** (i+1) - tupla[1] % (10 ** i)
      segundo_componente = tupla[0] % 10 ** (i+1) - tupla[0] % (10 ** i)
      suma = primer_componente + segundo_componente

      print(f'{primer_componente} + {segundo_componente} = {suma}')
      total += suma
      
    elif tupla[0] // (10 ** i) == 0:

      primer_componente = tupla[1] % 10 ** (i+1) - tupla[1] % (10 ** i)

      print(f'{primer_componente} + 0 = {primer_componente}')
      total += primer_componente


  return print(f'El Total es: {total}')

# Esta función es notable porque define una suma de 2 números pero utiliza la suma (signo +) para poder ejecutarse 😂
if __name__ == '__main__':

  print("Para sumar dos números podemos descomponerlos en base 10 \n")
  
  sumando_a = int(input('Ingresa un primer número positivo:'))
  sumando_b = int(input('Ingresa un segundo número positivo:'))

  suma_dificil(sumando_a, sumando_b)
