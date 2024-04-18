import os

class Producto:
    def __init__(instancia, codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor, stock_actual):
        instancia.codigo = codigo
        instancia.nombre = nombre
        instancia.valor_compra = valor_compra
        instancia.valor_venta = valor_venta
        instancia.stock_minimo = stock_minimo
        instancia.stock_maximo = stock_maximo
        instancia.proveedor = proveedor
        instancia.stock_actual = stock_actual

productos = []

def registrar_producto():
    try:
        codigo = input("Código del producto: ")
        nombre = input("Nombre del producto: ")
        valor_compra = float(input("Valor de compra: "))
        valor_venta = float(input("Valor de venta: "))
        stock_minimo = int(input("Stock mínimo permitido: "))
        stock_maximo = int(input("Stock máximo permitido: "))
        proveedor = input("Nombre del proveedor: ")
        stock_actual = int(input("Stock actual: "))

        producto = Producto(codigo, nombre, valor_compra, valor_venta, stock_minimo, stock_maximo, proveedor, stock_actual)
        productos.append(producto)
        print("Producto registrado exitosamente.")
    except ValueError:
        print("Error: Ingrese un valor válido para los campos numéricos.")

def visualizar_productos():
    if not productos:
        print("No hay productos registrados.")
        return
    print("\nLista de productos:")
    for producto in productos:
        ganancia_total_producto = (producto.valor_venta - producto.valor_compra) * producto.stock_actual
        print(f" Código: {producto.codigo}\n Nombre: {producto.nombre}\n Valor de compra: {producto.valor_compra}\n Valor de venta: {producto.valor_venta}\n Stock mínimo: {producto.stock_minimo}\n Stock máximo: {producto.stock_maximo}\n Proveedor: {producto.proveedor}\n Stock actual: {producto.stock_actual}\n Ganancia Total: ${ganancia_total_producto:.2f}\n")

def actualizar_stock():
    codigo_producto = input("Código del producto: ")
    producto = next((prod for prod in productos if prod.codigo == codigo_producto), None)
    if producto:
        try:
            nuevo_stock = int(input("Nuevo stock: "))
            if nuevo_stock < 0:
                print("El stock no puede ser negativo.")
            else:
                producto.stock_actual = nuevo_stock
                print("Stock actualizado correctamente.")
        except ValueError:
            print("Error: Ingrese un número válido.")
    else:
        print("Producto no encontrado.")

def calcular_ganancia_total():
    total_ganancia = 0
    for producto in productos:
        ganancia_por_producto = (producto.valor_venta - producto.valor_compra) * producto.stock_actual
        total_ganancia += ganancia_por_producto
    print(f"La ganancia potencial total es: ${total_ganancia:.2f}")

def informe_stock_minimo():
    print("\nProductos con stock bajo el mínimo:")
    for producto in productos:
        if producto.stock_actual < producto.stock_minimo:
            print(f" Código: {producto.codigo}\n Nombre: {producto.nombre}\n Stock actual: {producto.stock_actual}\n Stock mínimo: {producto.stock_minimo}\n")

def menu_principal():
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("\nMenú principal:")
        print("1. Registrar producto")
        print("2. Visualizar productos")
        print("3. Actualizar stock")
        print("4. Calcular ganancia total")
        print("5. Informe de stock mínimo")
        print("6. Salir")

        opcion = input("Ingrese una opción: ")
        if opcion == '1':
            registrar_producto()
        elif opcion == '2':
            visualizar_productos()
        elif opcion == '3':
            actualizar_stock()
        elif opcion == '4':
            calcular_ganancia_total()
        elif opcion == '5':
            informe_stock_minimo()
        elif opcion == '6':
            break
        else:
            print("Opción inválida.")
        input("Presiona Enter para continuar...")

menu_principal()
