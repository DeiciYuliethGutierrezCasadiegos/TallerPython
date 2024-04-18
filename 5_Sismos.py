import os

# Función para limpiar la pantalla
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para registrar una ciudad
def registrar_ciudad(ciudades, cantidad_sismos):
    limpiar_pantalla()
    ciudad = input("Ingrese el nombre de la ciudad: ")
    if ciudad not in ciudades:
        ciudades[ciudad] = [None] * cantidad_sismos
        print(f"Ciudad '{ciudad}' registrada correctamente.")
    else:
        print("¡La ciudad ya está registrada!")

# Función para registrar un sismo en una ciudad
def registrar_sismo(ciudades, cantidad_sismos):
    limpiar_pantalla()
    ciudad = input("Ingrese el nombre de la ciudad donde ocurrió el sismo: ")
    if ciudad in ciudades:
        for i in range(cantidad_sismos):
            if ciudades[ciudad][i] is None:
                magnitud = float(input(f"Ingrese la magnitud del sismo {i + 1} (0 para omitir): "))
                ciudades[ciudad][i] = magnitud
                print(f"Sismo {i + 1} registrado correctamente en la ciudad de {ciudad}.")
                break
            elif i == cantidad_sismos - 1:
                print("¡Ya se han registrado todos los sismos para esta ciudad!")
    else:
        print("La ciudad ingresada no está registrada.")

# Función para buscar sismos por ciudad
def buscar_sismos_por_ciudad(ciudades):
    limpiar_pantalla()
    ciudad = input("Ingrese el nombre de la ciudad para ver sus sismos: ")
    if ciudad in ciudades:
        print(f"Sismos registrados en la ciudad de {ciudad}:")
        for i, magnitud in enumerate(ciudades[ciudad], start=1):
            print(f"Sismo {i}: {magnitud if magnitud is not None else 'No registrado'}")
    else:
        print("La ciudad ingresada no está registrada.")

# Función para generar un informe de riesgo
def informe_de_riesgo(ciudades):
    limpiar_pantalla()
    print("Informe de riesgo:")
    for ciudad, sismos in ciudades.items():
        promedio = sum(sismo for sismo in sismos if sismo is not None) / len(sismos)
        print(f"Ciudad: {ciudad}")
        print(f"Promedio de magnitudes de sismos: {promedio:.2f}")
        if promedio < 2.5:
            print("Estado de riesgo: Amarillo (Sin riesgo)")
        elif 2.6 <= promedio <= 4.5:
            print("Estado de riesgo: Naranja (Riesgo medio)")
        else:
            print("Estado de riesgo: Rojo (Riesgo alto)")

# Función principal
def main():
    limpiar_pantalla()
    ciudades = {}
    cantidad_ciudades = 5
    cantidad_sismos = int(input("Ingrese la cantidad de sismos a registrar por ciudad: "))

    for _ in range(cantidad_ciudades):
        registrar_ciudad(ciudades, cantidad_sismos)

    while True:
        print("\nMenú:")
        print("1. Registrar Ciudad:")
        print("2. Registrar Sismo.")
        print("3. Buscar Sismos por Ciudad:")
        print("4. Informe de Riesgo:")
        print("5. Salir:")

        opcion = input("Seleccione una opción: ")
        limpiar_pantalla()

        if opcion == "1":
            registrar_ciudad(ciudades, cantidad_sismos)
        elif opcion == "2":
            registrar_sismo(ciudades, cantidad_sismos)
        elif opcion == "3":
            buscar_sismos_por_ciudad(ciudades)
        elif opcion == "4":
            informe_de_riesgo(ciudades)
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor seleccione una opción del menú.")

if __name__ == "__main__":
    main()
