# file_handler.py
# Handles reading and writing CSV files

import csv

def write_csv(inventory, path="data/inventory.csv", include_header=True):
    """
Saves the inventory to a CSV file.

Parameters:
    inventory (list): List of product dictionaries
    path (str): File path to save CSV
    include_header (bool): Whether to include header row

Returns:
    None
"""
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
    """
Reads a CSV file and validates its content.

Parameters:
    path (str): File path to read CSV

Returns:
    tuple: (list of valid products, number of invalid rows)
"""
    products = []
    invalid_rows = 0
    
    try:
        with open(path, mode="r", newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            
            # Validate header structure
            if reader.fieldnames != ["name", "price", "quantity"]:
                print("Invalid CSV header.")
                return [], 0

            for row in reader:
                try:
                    name = row["name"]
                    price = float(row["price"])
                    quantity = int(row["quantity"])

                    # Validate non-negative values
                    if price < 0 or quantity < 0:
                        raise ValueError

                    products.append({
                        "name": name,
                        "price": price,
                        "quantity": quantity
                    })

                except (ValueError, KeyError):
                    # Count invalid rows
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
    """
Loads inventory from a CSV file.

Allows user to overwrite or merge with current inventory.

Parameters:
    inventory (list): Current inventory
    path (str): File path to load CSV

Returns:
    list: Updated inventory
"""
    products, invalid_rows = read_csv(path)
    
    if not products:
        print("No valid products found. No updates added.")
        return inventory

    choice = input("Overwrite current inventory? (Y/N): ").strip().upper()

    if choice == "Y":
        # Replace inventory completely
        inventory = products
        action = "overwrite"
    else:
        # Merge inventories
        for prod in products:
            existing = next((p for p in inventory if p["name"] == prod["name"]), None)
            
            if existing:
                # Update quantity and price
                existing["quantity"] += prod["quantity"]
                existing["price"] = prod["price"]
            else:
                inventory.append(prod)

        action = "merge"
        
    print(f"\nInventory loaded successfully ({action}).")
    print(f"Products loaded: {len(products)}")
    print(f"Invalid rows skipped: {invalid_rows}")
    
    return inventory