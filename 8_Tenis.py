import os
import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect('torneo_tenis_mesa.db')
c = conn.cursor()

# Crear tabla de jugadores si no existe
c.execute('''
CREATE TABLE IF NOT EXISTS jugadores (
    id_jugador TEXT PRIMARY KEY,
    nombre TEXT,
    edad INTEGER,
    categoria TEXT,
    pj INTEGER DEFAULT 0,
    pg INTEGER DEFAULT 0,
    pp INTEGER DEFAULT 0,
    pa INTEGER DEFAULT 0,
    tp INTEGER DEFAULT 0
)
''')

# Categorías y requisitos de edad
categorias = {
    "Novato": (15, 16),
    "Intermedio": (17, 20),
    "Avanzado": (21, 100)
}

# Función para limpiar la consola
def clear_console():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

# Menú principal
while True:
    clear_console()
    print("Menú principal")
    print("1. Registrar jugador")
    print("2. Controlar juego")
    print("3. Ingresar resultados")
    print("4. Ver ganadores")
    print("5. Generar informe")
    print("6. Salir")

    opcion = input("Ingrese una opción (1-6): ")

    if opcion == "1":
        # Registrar jugador
        id_jugador = input("Ingrese el ID del jugador: ")
        nombre = input("Ingrese el nombre del jugador: ")
        edad = int(input("Ingrese la edad del jugador: "))

        # Validar edad y categoría
        categoria = None
        for cat, edades in categorias.items():
            if edades[0] <= edad <= edades[1]:
                categoria = cat
                break

        if categoria is None:
            print("El jugador no cumple con los requisitos de edad.")
        else:
            # Registrar jugador en la base de datos
            c.execute("INSERT INTO jugadores (id_jugador, nombre, edad, categoria) VALUES (?, ?, ?, ?)", (id_jugador, nombre, edad, categoria))
            conn.commit()
            print("Jugador registrado con éxito.")

    elif opcion == "2":
        # Controlar juego
        try:
            id_jugador1 = input("Ingrese el ID del jugador 1: ")
            id_jugador2 = input("Ingrese el ID del jugador 2: ")

            c.execute("SELECT * FROM jugadores WHERE id_jugador=? OR id_jugador=?", (id_jugador1, id_jugador2))
            jugadores = c.fetchall()
            if len(jugadores) != 2:
                raise ValueError("Uno o ambos jugadores no están registrados.")
            if jugadores[0][3] != jugadores[1][3]:
                raise ValueError("Los jugadores no pertenecen a la misma categoría.")

            ganador = input("Ingrese el ID del ganador: ")
            perdedor = ganador == id_jugador1 and id_jugador2 or id_jugador1

            # Actualizar registros de los jugadores en la base de datos
            c.execute("UPDATE jugadores SET pj=pj+1, pg=pg+1, pa=pa+2 WHERE id_jugador=?", (ganador,))
            c.execute("UPDATE jugadores SET pj=pj+1, pp=pp+1, tp=tp+2 WHERE id_jugador=?", (perdedor,))
            conn.commit()
            print("Resultados del juego actualizados con éxito.")

        except ValueError as e:
            print(e)

    elif opcion == "3":
        # Ingresar resultados
        categoria = input("Ingrese la categoría para ingresar resultados: ")
        num_partidos = int(input(f"Ingrese la cantidad de partidos jugados en la categoría {categoria}: "))

        for i in range(1, num_partidos + 1):
            id_jugador = input(f"Ingrese el ID del jugador {i}: ")
            pj = int(input("Ingrese la cantidad de partidos jugados: "))
            pg = int(input("Ingrese la cantidad de partidos ganados: "))
            pp = int(input("Ingrese la cantidad de partidos perdidos: "))
            pa = int(input("Ingrese la cantidad de puntos a favor: "))
            tp = int(input("Ingrese la cantidad de puntos en contra: "))

            # Actualizar registros del jugador en la base de datos
            c.execute("UPDATE jugadores SET pj=pj+?, pg=pg+?, pp=pp+?, pa=pa+?, tp=tp+? WHERE id_jugador=?", (pj, pg, pp, pa, tp, id_jugador))
            conn.commit()

    elif opcion == "4":
        # Ver ganadores
        print("Ganadores por categoría:")
        for categoria in categorias:
            c.execute("SELECT * FROM jugadores WHERE categoria=? ORDER BY pg DESC, pa DESC", (categoria,))
            jugadores_en_categoria = c.fetchall()
            if jugadores_en_categoria:
                ganador = jugadores_en_categoria[0]
                print(f"Ganador de la categoría {categoria}:")
                print(f"ID: {ganador[0]}")
                print(f"Nombre: {ganador[1]}")
                print(f"Edad: {ganador[2]}")
                print("-------------------------")
                print(f"PJ: {ganador[4]}")
                print(f"PG: {ganador[5]}")
                print(f"PP: {ganador[6]}")
                print(f"PA: {ganador[7]}")
                print(f"TP: {ganador[8]}")
                print("\n")

    elif opcion == "5":
        # Generar informe
        print("Informe de todos los jugadores:")
        c.execute("SELECT * FROM jugadores ORDER BY categoria, nombre")
        all_players = c.fetchall()
        for player in all_players:
            print(f"ID: {player[0]}, Nombre: {player[1]}, Categoria: {player[3]}, PJ: {player[4]}, PG: {player[5]}, PP: {player[6]}, PA: {player[7]}, TP: {player[8]}")
        print("\n")

    elif opcion == "6":
        # Salir
        print("Saliendo del programa.")
        conn.close()
        break
