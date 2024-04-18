import os



def limpiar_pantalla():

    # Limpia la pantalla de la consola

    if os.name == 'nt':  

        os.system('cls')

    else:

        os.system('clear')



def calcular_imc():

    limpiar_pantalla()

    registros = []  # Lista para almacenar los registros de personas

    estudiantes_peso_ideal = 0  # Contador de estudiantes con peso ideal

    estudiantes_obesidad_I = 0  # Contador de estudiantes con obesidad grado I

    estudiantes_obesidad_II = 0  # Contador de estudiantes con obesidad grado II

    estudiantes_obesidad_III = 0  # Contador de estudiantes con obesidad grado III

    estudiantes_sobrepeso = 0  # Contador de estudiantes con sobrepeso

    estudiantes_desnutricion = []  # Lista para almacenar estudiantes con desnutrición

    for i in range(20):

        print(f"Registro de la persona {i + 1}")

        nombre = input('Ingrese el nombre del estudiante: ')

        edad = int(input('Ingrese la edad del estudiante: '))

        peso = float(input('Ingrese el peso del estudiante (en kg): '))

        altura = float(input('Ingrese la altura del estudiante (en metros): '))



        # Calcula el IMC

        imc = peso // (altura ** 2)



        # Determina la categoría de peso según el IMC y actualiza los contadores

        if imc < 18.5:

            estudiantes_desnutricion.append({

                'Nombre': nombre,

                'Edad': edad,

                'Peso': peso,

                'Altura': altura,

                'IMC': imc,

            })

        elif 18.5 <= imc < 24.9:

            estudiantes_peso_ideal += 1

        elif 25 <= imc < 29.9:

            estudiantes_sobrepeso += 1

        elif 30 <= imc < 34.9:

            estudiantes_obesidad_I += 1

        elif 35 <= imc < 39.9:

            estudiantes_obesidad_II += 1

        elif imc >= 40:

            estudiantes_obesidad_III += 1



        # Guarda el registro en la lista

        registros.append({

            'Nombre': nombre,

            'Edad': edad,

            'Peso': peso,

            'Altura': altura,

            'IMC': imc,

        })

        print("-------------------------------------")



    # Muestra un resumen al final de los registros

    limpiar_pantalla()

    print("Resumen de Registros:")

    for i, registro in enumerate(registros, start=1):

        print(f"\nRegistro de la persona {i}")

        for clave, valor in registro.items():

            print(f"{clave}: {valor}")

    

    # Muestra la cantidad de estudiantes en cada categoría de peso

    print("\nCantidad de estudiantes en cada categoría de peso:")

    print("Peso Ideal:", estudiantes_peso_ideal)

    print("Sobrepeso:", estudiantes_sobrepeso)

    print("Obesidad Grado I:", estudiantes_obesidad_I)

    print("Obesidad Grado II:", estudiantes_obesidad_II)

    print("Obesidad Grado III:", estudiantes_obesidad_III)



    # Muestra el reporte de estudiantes con desnutrición

    print("\nReporte de estudiantes con desnutrición:")

    for estudiante in estudiantes_desnutricion:

        print("\nNombre:", estudiante['Nombre'])

        print("Edad:", estudiante['Edad'])

        print("Peso:", estudiante['Peso'])

        print("Altura:", estudiante['Altura'])

        print("IMC:", estudiante['IMC'])



if __name__ == "__main__":

    calcular_imc()

