# Inventory Service Module
# This module contains all the logic for managing the inventory.

def add_product(inventory, name, price, quantity):
    
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)

def show_inventory(inventory):
    # Check if inventory is empty before printing
    if not inventory:
        print("Inventory is empty.")
        return
    
    print(f"\nInventory")
    
    # Iterate through each product and display its details
    for product in inventory:
        print(f"Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
        
def search_product(inventory, name):

    for product in inventory: 
        if product["name"]== name:
            return product
    return None

def update_product(inventory, name, new_price=None, new_quantity=None):
    product = search_product(inventory, name)
    if product: 
        if new_price is not None:
            product["price"] = new_price
        if new_quantity is not None:
            product["quantity"] = new_quantity
        print("Product updated successfully")
    else:
        print("Product not found")

def delete_product(inventory, name):
    product = search_product(inventory, name)
    if product:
        inventory.remove(product)
        print("Product successfully deleted. ")
    else:
        print("Product not found")

def calculate_stats(inventory):
    if not inventory:
        return None
    total_value = 0
    total_products = 0
    most_expensive = None
    highest_stock = None
    
    for product in inventory:
        total_value+= product["price"] * product["quantity"]
        total_products += product["quantity"]
        
        if most_expensive is None or product["price"] > most_expensive["price"]:
            most_expensive = product["name"], product["price"]
        if highest_stock is None or product["quantity"] > highest_stock["quantity"]:
            highest_stock = product["name"]
    return {
        "total_units": total_products,
        "total_value": total_value,
        "most_expensive": most_expensive,
        "highest_stock": highest_stock
        } 