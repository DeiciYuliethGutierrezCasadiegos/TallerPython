import os

def limpiar_pantalla():
    # Limpia la pantalla de la consola
    if os.name == 'nt':  # Verifica si el sistema es Windows
        os.system('cls')
    else:
        os.system('clear')

def calcular_imc():
    limpiar_pantalla()
    nombre = input('Ingrese el nombre del estudiante: ')
    edad = int(input('Ingrese la edad del estudiante: '))
    peso = float(input('Ingrese el peso del estudiante (en kg): '))
    altura = float(input('Ingrese la altura del estudiante (en metros): '))

    # Calcula el IMC
    imc = peso // (altura ** 2)

    # Imprime los detalles del estudiante y su IMC
    print('\nNombre del estudiante:', nombre)
    print('Edad del estudiante:', edad)
    print('IMC del estudiante:', imc)

    # Determina la categoría de peso según el IMC
    if 18.5 <= imc < 24.9:
        print('CATEGORÍA: NORMAL')
    elif 25 <= imc < 29.9:
        print('CATEGORÍA: SOBREPESO')
    elif 30 <= imc < 34.9:
        print('CATEGORÍA: OBESIDAD I')
    elif 35 <= imc < 49.9:
        print('CATEGORÍA: OBESIDAD II')
    elif imc >= 40:
        print('CATEGORÍA: OBESIDAD III')

if __name__ == "__main__":
    calcular_imc()
