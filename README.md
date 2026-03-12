# Simple Inventory Program

## Description
This Python Basic program allows the user to register a product by entering its **name**, **price**, and **quantity**. So it does allow to enter the **customer_name** as a first input. 
It calculates the **total cost** of the product and displays a **formatted invoice** in the console. 
The program includes **input validation** to ensure that the price and quantity are numeric and non-negative. 
Decimals are displayed **only if necessary**, by adding :g at the end of the output functions over the float variables, making the invoice clean and easy to read.

## Features
- Ask the user for product name, price, and quantity
- Validate that price and quantity are numeric and not negative
- Calculate total cost (price * quantity)
- Display a clear invoice in console format
- Format numbers to show decimals only when needed
- Reusable function print_invoice() to print any product's invoice

By runing the code and entering with the keyboard all the required information, it prompts an invoice that looks like this:

=======INVOICE======
Customer name: Arley
Product: Bread
Price: $1235.5
Quantity: 6
Final total: $7411

Thank you for your purchase

====================

