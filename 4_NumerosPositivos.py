def generar_reporte(numeros):
  # Total de números ingresados
  total_numeros = len(numeros)

  # Separación de números pares e impares
  numeros_pares = [num for num in numeros if num % 2 == 0]
  numeros_impares = [num for num in numeros if num % 2 != 0]

  # Cantidad de números menores que 10
  numeros_menores_10 = sum(1 for num in numeros if num < 10)

  # Cantidad de números entre 20 y 50
  numeros_entre_20_y_50 = sum(1 for num in numeros if 20 <= num <= 50)

  # Cantidad de números mayores que 100
  numeros_mayores_100 = sum(1 for num in numeros if num > 100)

  # Cálculo del total de pares e impares
  total_pares = len(numeros_pares)
  total_impares = len(numeros_impares)

  # Cálculo del promedio de pares e impares (evitando división por cero)
  promedio_pares = sum(numeros_pares) / total_pares if total_pares > 0 else 0
  promedio_impares = sum(numeros_impares) / total_impares if total_impares > 0 else 0

  # Impresión del reporte
  print("Reporte:")
  print("a. Total de números ingresados:", total_numeros)
  print("b. Total de números pares ingresados:", total_pares)
  print("c. Promedio de los números pares:", promedio_pares)
  print("d. Promedio de los números impares:", promedio_impares)
  print("e. Cuántos números son menores que 10:", numeros_menores_10)
  print("f. Cuántos números están entre 20 y 50:", numeros_entre_20_y_50)
  print("g. Cuántos números son mayores que 100:", numeros_mayores_100)

def main():
  # Lista para almacenar los números ingresados por el usuario
  numeros = []

  # Bucle para la entrada de números, se detiene cuando se ingresa un número negativo
  while True:
      numero = int(input("Ingrese un número entero positivo (ingrese un número negativo para finalizar): "))
      if numero < 0:
          break
      numeros.append(numero)

  # Si se ingresaron números, se genera el reporte
  if numeros:
      generar_reporte(numeros)
  else:
      print("No se ingresaron números.")

if __name__ == "__main__":
  main()
  
