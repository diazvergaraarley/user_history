# importar la función principal del menú desde el archivo menu.py
from menu import main_menu

# verificar si este archivo se está ejecutando directamente
# (y no siendo importado desde otro archivo)
if __name__ == "__main__":
    
    # ejecutar la función principal del programa (menú interactivo)
    main_menu()
    