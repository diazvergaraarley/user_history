# ================================
# Simple Inventory Program
# ================================
# Objective:
# Register products with name, price, and quantity,
# calculate total cost, and display a clear invoice.

#Task# 2: Imput data:

    #Ask the customer name: (included to enhance the code)

customer_name= input("Enter customer name: ")

    #Ask the product name:

name = input("Enter the product name: ")

    #Input and Validate price

while True:
    price_input =input("Enter the product price: ")
    try:
        price = float(price_input) #convert to float
        if price <=0: 
            print("Price out of range. Try again.") #ensure the number is not negative or zero
        else: 
            break #exit the loop if valid
    except ValueError:
        print("Invalid input. Please enter a valid price") #ensure the input is a number

while True:
    quantity_input= input("Enter the product quantity: ")
    try:
        quantity = int(quantity_input) #convert input to integer
        if quantity <= 0: 
            print("Price out of range. Try again.")
        else:
            break # exit the loop if valid
    except ValueError:
        print("Invalid input. Please enter a valid quantity") #ensure the input is a number

#Task #3: Total Cost:

    #Calculate the total cost

total_cost= price * quantity #multiply the price by the quantity of product to get the total cost

def print_invoice(customer_name, name, price, quantity, total_cost): #define invoice variable with the bill elements so we include it in a function to print every data with one "print" use
    invoice= f"""=======INVOICE======
Customer name: {customer_name}
Product: {name}
Price: ${price:g}
Quantity: {quantity}
Final total: ${total_cost:g}

Thank you for your purchase

===================="""
    print(invoice)

print_invoice(customer_name, name, price, quantity, total_cost) 
#call the function so it "prints" the bill using the existing data included in function already defined.


#Task #5: General program description:

# This program allows the user to register a product by entering its name,
# price, and quantity. It validates that the price and quantity are numeric
# and non-negative. Then it calculates the total cost (price * quantity)
# and prints a formatted invoice showing all the details in a clear manner.
#