# Lista donde se almacenarán los productos
inventario = []

# Función para mostrar el menú y validar la opción
def menu():
    while True:
        print("\n--- MENÚ ---")
        print("1 - Agregar producto")
        print("2 - Mostrar inventario")
        print("3 - Calcular estadísticas")
        print("4 - Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion in [1, 2, 3, 4]:
                return opcion
            else:
                print("Opción inválida. Intente de nuevo.")
        except ValueError:
            print("Error: debe ingresar un número.")

# Función para agregar productos al inventario
def agregar_producto():
    nombre = input("Ingrese el nombre del producto: ")
    
    try:
        precio = float(input("Ingrese el precio: "))
        cantidad = int(input("Ingrese la cantidad: "))
    except ValueError:
        print("Error: precio o cantidad inválidos.")
        return

    producto = {
        "nombre": nombre,
        "precio": precio,
        "cantidad": cantidad
    }

    inventario.append(producto)
    print("Producto agregado correctamente.")

# Función para mostrar el inventario
def mostrar_inventario():
    if not inventario:
        print("El inventario está vacío.")
        return

    print("\n--- INVENTARIO ---")
    for producto in inventario:
        print(f"Producto: {producto['nombre']} | Precio: {producto['precio']} | Cantidad: {producto['cantidad']}")

# Función para calcular estadísticas
def calcular_estadisticas():
    if not inventario:
        print("No hay productos para calcular estadísticas.")
        return

    valor_total = 0
    total_productos = 0

    for producto in inventario:
        valor_total += producto["precio"] * producto["cantidad"]
        total_productos += producto["cantidad"]

    print("\n--- ESTADÍSTICAS ---")
    print(f"Valor total del inventario: {valor_total}")
    print(f"Cantidad total de productos: {total_productos}")

# Bucle principal del programa
while True:
    opcion = menu()

    if opcion == 1:
        agregar_producto()
    elif opcion == 2:
        mostrar_inventario()
    elif opcion == 3:
        calcular_estadisticas()
    elif opcion == 4:
        print("Saliendo del programa...")
        break
    else:
        print("Opción inválida.")

# Comentario final:
# Este programa permite gestionar un inventario básico utilizando listas y diccionarios.
# Se aplican estructuras de control como condicionales, bucles y funciones para organizar el código.