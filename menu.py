# importar módulo para trabajar con fechas y horas
import datetime



# importar todas las funciones del archivo customer_services
from services.customer_services import *

# importar funciones para manejo de archivos (leer/escribir CSV)
from utils.file_handler import *


# función para mostrar mensajes con marca de tiempo (timestamp)
def show_timestapm(message):
    
    # obtener fecha y hora actual en formato legible
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # imprimir mensaje junto con el timestamp
    print (f"\n[{now}] {message}")
    

# función principal del menú
def main_menu():
    
    # cargar registros desde el archivo CSV (si existe)
    records = load_cust_list([])
    
    # bucle infinito para mantener el menú activo
    while True:
        
        # mostrar inicio del menú con timestamp
        show_timestapm("\nCustomer records menu started")
        
        # mostrar opciones del menú
        print("""\n
              ---- WDY Gym Menu ----
              1. Create new customer record.
              2. Show current customers records. 
              3. Search customer.
              4. Update customer. 
              5. Delete customer.
              6. Exit menu.\n
              """)
        
        try:
            # pedir opción al usuario
            choice = input("Select an option (1-6): ").strip()
            
            
            # ---------------- OPCIÓN 1: CREAR CLIENTE ----------------
            if choice == "1":
                print("\n")
                
                # validar ID (solo números positivos)
                id = input_positive_int("Enter Customer ID: ")
                
                # validar nombre (solo letras y espacios)
                name = input_name("Enter Customer name: ")
                
                # validar edad (número positivo)
                age = input_positive_int("Enter customer age: ")
                
                # diccionario de tipos de plan
                plan = input_plan()
     
                # diccionario de estados del cliente
                status = input_status()
                
                # agregar cliente a la lista
                add_customer(records, id, name, age, plan, status)
                
                # mostrar mensaje con timestamp
                show_timestapm(f"Customer '{name}' added. ")
                
                # guardar cambios en el archivo CSV
                write_records(records)
            
            
            # ---------------- OPCIÓN 2: MOSTRAR CLIENTES ----------------
            elif choice == "2":
                print("\n")
                
                # mostrar todos los registros
                show_cust_rec(records)
                
            
            # ---------------- OPCIÓN 3: BUSCAR CLIENTE ----------------
            elif choice == "3":
                print("\n")
                
                # pedir ID a buscar
                id = int(input("Enter ID # to search customer: ").strip())
                
                # buscar cliente
                customer = search_cust(records, id)
                
                # mostrar resultado
                #si customer se corresponde con un valor, llama a la variable como un diccionario
                if customer:
                    print(f"{customer}")
                #Si no encuentra nada, arroja el mensaje de no encontrado
                else:
                    print("Customer not found. ")
            
            
            # ---------------- OPCIÓN 4: ACTUALIZAR CLIENTE ----------------
            elif choice == "4":
                print("\n")
                
                try:
                    # pedir ID del cliente a actualizar
                    id_input = input("Enter ID from customer you want to update: ").strip()
                    id = int(id_input)

                    # buscar cliente
                    customer = search_cust(records, id)
                    
                    if not customer:
                        print("Customer not found.")
                        continue
                    
                    # pedir nuevos datos (opcional)
                    new_name = input("New Name (leave blank to skip): ").strip()

                    new_age_input = input("New Age (leave blank to skip): ").strip()
                    new_age = int(new_age_input) if new_age_input else None

                    new_plan = input("New Plan (leave blank to skip): ").strip()
                    new_status = input("New Status (leave blank to skip): ").strip()

                    # actualizar datos del cliente
                    update_cust_info(
                        records,
                        id,
                        new_name=new_name if new_name else None,
                        new_age=new_age,
                        new_plan=new_plan if new_plan else None,
                        new_status=new_status if new_status else None
                    )

                    # guardar cambios
                    write_records(records)

                except ValueError:
                    print("\n")
                    print("Invalid input. ID and age must be numbers.")

                
            # ---------------- OPCIÓN 5: ELIMINAR CLIENTE ----------------
            elif choice == "5":
                print("\n")
                
                # pedir ID del cliente a eliminar
                id = int(input("Enter the ID from the customer you want to delete. ").strip())
                
                # eliminar cliente
                delete_cust(records, id)
                
                # guardar cambios
                write_records(records)
            
            
            # ---------------- OPCIÓN 6: SALIR ----------------
            elif choice == "6":
                print("\n")
                
                # mostrar mensaje de cierre
                show_timestapm(f"\nClosing program...")
                break
            
            
            # opción inválida
            else:
                print("\n")
                print("Invalid option. Enter a number between 1-6.")
        
        
        # error si el input no es válido
        except ValueError:
            print("\n")
            print("Invalid option.")
        
        # captura cualquier otro error inesperado
        except Exception as e:
            print("\n")
            print(f"Invalid option. {e}")