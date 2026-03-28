# Inventory Service Module
# Contains all business logic for inventory management

def add_product(inventory, name, price, quantity):
    """
    Adds a new product to the inventory.

    Parameters:
        inventory (list): List of product dictionaries
        name (str): Product name
        price (float): Product price
        quantity (int): Product quantity

    Returns:
        None
    """
    product = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)

def show_inventory(inventory):
    """
Displays all products in the inventory.

Parameters:
    inventory (list): List of product dictionaries

Returns:
    None
"""
    if not inventory:
        print("Inventory is empty.")
        return
    
    print(f"\nInventory")
    
    # Print all products
    for product in inventory:
        print(f"Product: {product['name']} | Price: {product['price']} | Quantity: {product['quantity']}")
        
def search_product(inventory, name):
    """
Searches for a product by name.

Parameters:
    inventory (list): List of product dictionaries
    name (str): Product name to search

Returns:
    dict or None: Found product or None if not found
"""
    for product in inventory: 
        if product["name"] == name:
            return product
    return None

def update_product(inventory, name, new_price=None, new_quantity=None):
    """
Updates a product's price and/or quantity.

Parameters:
    inventory (list): List of product dictionaries
    name (str): Product name
    new_price (float, optional): New price
    new_quantity (int, optional): New quantity

Returns:
    None
"""
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
    """
Deletes a product from the inventory.

Parameters:
    inventory (list): List of product dictionaries
    name (str): Product name

Returns:
    None
"""
    product = search_product(inventory, name)
    if product:
        inventory.remove(product)
        print("Product successfully deleted.")
    else:
        print("Product not found")

def calculate_stats(inventory):
    """
Calculates inventory statistics.

Parameters:
    inventory (list): List of product dictionaries

Returns:
    dict: Contains total_units, total_value,
          most_expensive (name, price),
          highest_stock (name, quantity)
"""
    if not inventory:
        return None

    total_value = 0
    total_products = 0
    most_expensive = None
    highest_stock = None
    
    for product in inventory:
        total_value += product["price"] * product["quantity"]
        total_products += product["quantity"]
        
        # Find most expensive product
        if most_expensive is None or product["price"] > most_expensive[1]:
            most_expensive = (product["name"], product["price"])
        
        # Find product with highest quantity
        if highest_stock is None or product["quantity"] > (
            next(p for p in inventory if p["name"] == highest_stock)["quantity"]
            if isinstance(highest_stock, str) else -1
        ):
            highest_stock = product["name"]

    return {
        "total_units": total_products,
        "total_value": total_value,
        "most_expensive": most_expensive,
        "highest_stock": highest_stock
    }