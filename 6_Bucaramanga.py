instalaciones = {}

def registrar_dependencia():
    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    instalaciones[nombre_dependencia] = {}

def registrar_consumo():
    nombre_dependencia = input("Ingrese el nombre de la dependencia: ")
    if nombre_dependencia not in instalaciones:
        print("La dependencia no ha sido registrada.")
        return

    dispositivo = input("Ingrese el nombre del dispositivo: ")
    while True:
        try:
            consumo = float(input("Ingrese el valor consumido por el dispositivo: "))
            if consumo < 0:
                print("El consumo no puede ser negativo. Inténtelo de nuevo.")
            else:
                break
        except ValueError:
            print("Por favor, ingrese un número válido.")

    instalaciones[nombre_dependencia][dispositivo] = consumo

def ver_CO2_producido():
    co2_producido = 0
    for dependencia, dispositivos in instalaciones.items():
        for consumo in dispositivos.values():
            co2_producido += consumo
    print("La cantidad total de CO2 producido es:", co2_producido)

def dependencia_mayor_CO2():
    max_CO2_producido = 0
    dependencia_mayor = None
    for dependencia, dispositivos in instalaciones.items():
        co2_producido = sum(dispositivos.values())
        if co2_producido > max_CO2_producido:
            max_CO2_producido = co2_producido
            dependencia_mayor = dependencia
    if dependencia_mayor:
        print("La dependencia que produce mayor CO2 es:", dependencia_mayor)
    else:
        print("No se han registrado dependencias.")

def menu_principal():
    opcion = 0
    while opcion != 5:
        print("\n--- Menú Principal ---")
        print("1. Registrar Dependencia")
        print("2. Registrar Consumo por Dependencia")
        print("3. Ver CO2 Producido")
        print("4. Dependencia que Produce Mayor CO2")
        print("5. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
        except ValueError:
            print("Por favor ingrese un número válido.")
            continue

        if opcion == 1:
            registrar_dependencia()
        elif opcion == 2:
            registrar_consumo()
        elif opcion == 3:
            ver_CO2_producido()
        elif opcion == 4:
            dependencia_mayor_CO2()
        elif opcion == 5:
            print("Saliendo del programa...")
        else:
            print("Opción inválida. Inténtelo nuevamente.")

menu_principal()
