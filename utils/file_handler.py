#file handler
import csv

def write_csv(inventory, path="data/inventory.csv", include_header=True):
    if not inventory:
        print("Cannot save. Inventory is empty.")
        return
    try:
        with open(path, mode="w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            
            if include_header:
                writer.writerow(["name", "price", "quantity"])
                
            for product in inventory:
                writer.writerow([product["name"], product["price"], product["quantity"]])
        print(f"Inventory saved successfully in: {path}")
    
    except PermissionError:
        print("Permission denied: cannot write to the file.")
        
    except Exception as e:
        print(f"An error occurred while saving: {e}")
        
def read_csv(path="data/inventory.csv"):
    products = []
    invalid_rows = 0
    
    try:
        with open(path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            
            if reader.fieldnames != ["name", "price", "quantity"]:
                print("Invalid CSV header.")
                return [], 0
            for row in reader:
                try:
                    name = row["name"]
                    price = float(row["price"])
                    quantity = int(row["quantity"])
                    if price < 0 or quantity < 0:
                        raise ValueError
                    products.append({"name": name, "price": price, "quantity": quantity})
                except (ValueError, KeyError):
                    invalid_rows += 1
        return products, invalid_rows
    except FileNotFoundError:
        print("File not found.")
        return [], 0
    except UnicodeDecodeError:
        print("File cannot be decoded.")
        return [], 0
    except Exception as e:
        print(f"An error ocurred while loading: {e}")
        return [], 0

def load_inventory_from_csv(inventory, path="data/inventory.csv"):
    products, invalid_rows = read_csv(path)
    
    
    if not products:
        print("No valid products found. No updates added. ")
        return inventory
    choice = input("Overwrite current inventory? (Y/N): ").strip().upper()
    if choice == "Y":
        inventory = products
        action = "overwrite"
    else:
        for prod in products:
            existing = next((p for p in inventory if p["name"] == prod["name"]), None)
            if existing:
                # sumar cantidad y actualizar precio
                existing["quantity"] += prod["quantity"]
                existing["price"] = prod["price"]
            else:
                inventory.append(prod)
        action = "merge"
        
    print(f"\nInventory loaded successfully ({action}).")
    print(f"Products loaded: {len(products)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    
    return inventory