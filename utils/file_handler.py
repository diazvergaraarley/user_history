# llamar CSV para que funcionen los parametros de csv
import csv

# definir variable para guardar "Escribir" los datos
# (parámetros: lista de diccionarios, ruta del archivo, include_header=True para incluir encabezado)
def write_records(records, path="data/customers.csv", include_header= True): 
    
    # bucle de validación / manejo de errores
    try:
        # with open() abre el archivo de forma segura y lo cierra automáticamente al terminar
        # mode="w" indica modo escritura (sobrescribe el archivo)
        # newline="" evita líneas en blanco extra en CSV
        # encoding="utf-8" asegura compatibilidad de caracteres
        with open(path, mode= "w", newline="", encoding="utf-8") as f:
            
            # csv.writer permite escribir filas en el archivo CSV
            writer= csv.writer(f)
            
            # si include_header es True, se escribe la fila de encabezados
            if include_header:
                writer.writerow(["id", "name", "age", "plan" ,"status"])
            
            # recorrer cada cliente en la lista records
            for customer in records:
                # escribir cada cliente como una fila en el CSV
                writer.writerow([
                    customer["id"], 
                    customer["name"], 
                    customer["age"], 
                    customer["plan"], 
                    customer["status"]
                ])
        
        # mensaje de éxito
        print(f"Customer succesfully saved in records")
    
    # error si no hay permisos de escritura
    except PermissionError:
        print("Permission denied: cannot write to the file.")
    
    # captura cualquier otro error
    except Exception as e:
        print(f"An error occurred while saving: {e}")


# función para leer clientes desde el CSV
def read_cust_list(path="data/customers.csv"):
    
    # lista donde se guardarán los registros válidos
    records = []
    
    # contador de filas inválidas
    invalid_rows = 0
    
    try:
        # abrir archivo en modo lectura
        with open(path, mode="r", newline="", encoding="utf-8") as f:
            
            # DictReader convierte cada fila en diccionario
            reader= csv.DictReader(f)
            
            # validar que el encabezado sea correcto
            if reader.fieldnames != ["id", "name", "age", "plan", "status"]:
                print("Invalid header.")
                return [], 0
            
            # recorrer cada fila del archivo
            for row in reader:
                try:
                    # convertir y validar tipos de datos
                    id = int(row["id"])
                    name = str(row["name"])
                    age = int(row["age"])
                    plan = str(row["plan"])
                    status = str(row["status"])
                    
                    # validar que id y edad no sean negativos
                    if id < 0 or age < 0:
                        raise ValueError
                    
                    # agregar registro válido a la lista
                    records.append({
                        "id": id,
                        "name": name,
                        "age": age,
                        "plan": plan,
                        "status": status
                    })
                
                # si hay error de conversión o falta de datos
                except (ValueError, KeyError):
                    invalid_rows += 1
        
        # devolver registros válidos y cantidad de inválidos
        return records, invalid_rows
    
    # error si el archivo no existe
    except FileNotFoundError:
        print("File not found. ")
        return [], 0
    
    # error si el archivo no se puede decodificar
    except UnicodeDecodeError:
        print("File cannot be decoded.")
        return [], 0

    # cualquier otro error
    except Exception as e:
        print(f"An error ocurred while loading: {e}")
        return [], 0


# función para cargar y actualizar la lista de clientes existente
def load_cust_list(records, path="data/customers.csv"):
    
    # leer datos del archivo
    file_records, invalid_rows = read_cust_list(path)
    
    # si no hay registros válidos, no se hace nada
    if not file_records:
        print("No valid customers found. No updates added.")
        return records
    
    # recorrer los registros del archivo
    for cust in file_records:
        
        # buscar si el cliente ya existe en la lista (por id)
        existing = next((p for p in records if p["id"] == cust["id"]), None)
        
        # si existe, actualizar sus datos
        if existing:
            existing["name"] = cust["name"]
            existing["age"] = cust["age"]
            existing["plan"] = cust["plan"]
            existing["status"] = cust["status"]
        
        # si no existe, agregarlo a la lista
        else:
            records.append(cust)
    
    # mensajes de resultado
    print(f"Customers records successfully loaded.")
    print(f"Customers loaded: {len(records)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    
    # devolver la lista actualizada
    return records