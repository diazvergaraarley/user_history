# Inventory: This list stores all the products added by the user.
inventory = []

# The 'menu' function displays the available options to the user.
# It runs inside an infinite loop until a valid option (1–4) is selected.
def menu():
    while True:
        print(f"""\n
        ----MENU----
        1. Add product
        2. Open inventory
        3. See calculations
        4. Exit\n""")
        try:
            # The user must input a number corresponding to a menu option
            option= int(input("Please select an option: "))
            
            # Validate that the option is one of the allowed values
            if option in [1,2,3,4]:
                return option
            else:
                # If the number is outside valid options
                print("Invalid option, try again.")
        
        except ValueError:
            # If the input is not a number, an error is shown and loop continues
            print("Invalid option, try again.")
            continue

# This function collects product data and adds it to the inventory list
def add_product(): 
    product_name = input("Enter the product name: ")
    try:
        # Convert price to float and quantity to integer
        price = float(input("Enter the product price: "))
        quantity= int(input("Enter the quantity: "))
    except ValueError:
        # If conversion fails, the function exits early
        print("Enter a valid option ")
        return
    
    # Product is stored as a dictionary
    product = {
        "name": product_name,
        "price": price,
        "quantity": quantity
    }

    # The product is appended to the global inventory list
    inventory.append(product)
    print("Product succesfully added")

# This function prints all products stored in the inventory
def open_inventory():
    # Check if inventory is empty before printing
    if not inventory:
        print("Inventory is empty.")
        return
    
    print(f"\nInventory")
    
    # Iterate through each product and display its details
    for product in inventory:
        print(f"Product: {product["name"]} | Price: {product["price"]} | Quantity: {product["quantity"]}")

# This function calculates total quantity and total inventory value
def see_calculations():
    # Prevent calculations if inventory is empty
    if not inventory:
        print("Nothing to calculate")
        return
    
    total_value = 0
    total_products = 0

    # Loop through inventory to accumulate totals
    for product in inventory:
        total_value+= product["price"] * product["quantity"]
        total_products += product["quantity"]

    # Display results
    print(f"""\nStats:
        Total products added: {total_products}
        Total Purchase ammount: {total_value}
        """)

# Main program loop: keeps running until the user chooses to exit
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
        # This should never happen due to validation in menu()
        print("Invalid option")