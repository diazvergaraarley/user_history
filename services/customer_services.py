# importar módulo para validaciones con expresiones regulares
import re

# función para agregar un nuevo cliente a la lista
def add_customer(records, id, name, age, plan, status):
    
    # validar si ya existe un cliente con el mismo id usando la función search_cust
    if search_cust(records, id):
        print("Customer with this ID already exists.")
        return
    
    # crear el diccionario con los datos del cliente
    customer = {
        "id" : id,
        "name": name,
        "age": age,
        "plan": plan,
        "status": status
    }
    
    # agregar el nuevo cliente a la lista
    records.append(customer)


# función para mostrar todos los registros de clientes
def show_cust_rec(records):
    
    # validar si la lista está vacía
    if not records:
        print("Customer records empty.")
        return
    
    # título de la sección
    print(f"\n Customer Records")
    
    # recorrer cada cliente e imprimir sus datos
    for customer in records:
        print(f"Id: {customer['id']}, Name: {customer['name']}, Age: {customer['age']}, Plan: {customer['plan']}, Status: {customer['status']}")
    
    # mostrar total de clientes registrados
    print(f"\n Total customers registered: {len(records)}")


# función para buscar un cliente por id
def search_cust(records, id):
    
    # recorrer la lista de clientes
    for customer in records:
        
        # comparar el id del cliente con el id buscado
        if customer["id"] == id:
            return customer  # retorna el cliente si lo encuentra
    
    # retorna None si no encuentra el cliente
    return None


# función para actualizar la información de un cliente
def update_cust_info(records, id, new_id= None, new_name=None, new_age=None, new_plan=None, new_status= None):
    
    # buscar el cliente por id
    customer= search_cust(records, id)
    
    # si el cliente existe, actualizar solo los campos enviados
    if customer:
        if new_id is not None:
            customer["id"] = new_id
        if new_name is not None:
            customer["name"] = new_name
        if new_age is not None:
            customer["age"] = new_age
        if new_plan is not None:
            customer["plan"] = new_plan
        if new_status is not None:
            customer["status"] = new_status
    
    # si no existe el cliente
    else:
        print("Customer not found")


# función para eliminar un cliente por id
def delete_cust(records, id):
    
    # buscar el cliente
    customer = search_cust(records, id)
    
    # si existe, eliminarlo de la lista
    if customer:
        records.remove(customer)
        print("Customer successfully removed from records.")
    
    # si no se encuentra el cliente
    else:
        print("Customer not found")
        
# función para solicitar un número entero positivo
def input_positive_int(message): 
    
    # bucle infinito hasta que el usuario ingrese un valor válido
    while True:
        try:
            # pedir input y convertirlo a entero
            value = int(input(message))
            
            # validar que sea mayor que 0
            if value <= 0:
                print("Invalid: must be greater than 0")
                continue
            
            # retornar el valor válido
            return value
        
        # manejar error si no se ingresa un número
        except ValueError:
            print("Error: must be a number")





# función para validar nombres (solo letras y espacios)
def input_name(message):
    
    # bucle hasta que el nombre sea válido
    while True:
        
        # pedir input y eliminar espacios al inicio y final
        name = input(message).strip()
        
        # validar con expresión regular (incluye acentos y ñ)
        if re.fullmatch(r"[A-Za-zÁÉÍÓÚáéíóúÑñ ]+", name):
            
            # retornar nombre válido
            return name
        
        else:
            print("Invalid name: only letters and spaces allowed")
            

# función para seleccionar tipo de plan
def input_plan():
    
    # diccionario que mapea abreviaciones a nombres completos
    plans = {
        "mo": "monthly",
        "qa": "quarterly",
        "ba": "biannual",
        "an": "annual"
    }

    # bucle hasta que el usuario elija una opción válida
    while True:
        
        # pedir opción, convertir a minúsculas y limpiar espacios
        choice = input("Enter plan (mo/qa/ba/an): ").lower().strip()
        
        # validar si la opción existe en el diccionario
        if choice in plans:
            
            # retornar el valor correspondiente (no la clave)
            return plans[choice]
        
        else:
            print("Invalid plan type")


# función para seleccionar estado del cliente
def input_status():
    
    # diccionario de opciones de estado
    status_map = {
        "a": "active",
        "i": "inactive"
    }

    # bucle hasta recibir una opción válida
    while True:
        
        # pedir input y normalizarlo
        choice = input("Enter status (a/i): ").lower().strip()
        
        # validar si la opción es correcta
        if choice in status_map:
            
            # retornar estado correspondiente
            return status_map[choice]
        
        else:
            print("Invalid status")