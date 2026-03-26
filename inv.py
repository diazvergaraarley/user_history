
inventory = []

def menu():
    while True:
        print(f"""\n
        ----MENU----
        1. Add product
        2. Open inventory
        3. See calculations
        4. Exit\n""")
        try:
            option= int(input("Please select an option:"))
            if option in [1,2,3,4]:
                return option
            else:
                print("Invalid option, try again.")
        except ValueError:
            print("Must be a number")
            continue
def add_product():
    product_name = input("Enter the product name: ")
    try:
        price = float(input("Enter the product price: "))
        quantity= int(input("Enter the quantity: "))
    except ValueError:
        print("Enter a valid number")
        return
    
    product = {
        "name": product_name,
        "price": price,
        "quantity": quantity
    }
    inventory.append(product)
    print("Product succesfully added")
def open_inventory():
    if not inventory:
        print("Inventory is empty.")
        return
    print(f"\nInventory")
    for product in inventory:
        print(f"Product: {product["name"]} | Price: {product["price"]} | Quantity: {product["quantity"]}")
def see_calculations():
    if not inventory:
        print("Nothing to calculate")
        return
    total_value = 0
    total_products = 0
    for product in inventory:
        total_value+= product["price"] * product["quantity"]
        total_products += product["quantity"]
    print(f"""\nStats:
        Total products added: {total_products}
        Total Purchase ammount: {total_value}
        """)


while True:
    option = menu()
    if option == 1:
        add_product()
    elif option == 2:
        open_inventory()
    elif option == 3:
        see_calculations()
    elif option == 4:
        print("Closing program...")
        break
    else:
        print("Invalid option")
