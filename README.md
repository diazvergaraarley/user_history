# Simple Inventory Program

## Description
This project is a simple Python console-based inventory system.  
It allows users to add products, view the inventory, and calculate basic statistics.

The program is designed for beginners to practice key programming concepts such as
user input, validation, loops, functions, and data structures like lists and dictionaries.

## How it works

1. The program displays a menu with four options:
   - Add product
   - Open inventory
   - See calculations
   - Exit

2. The user selects an option by entering a number (1–4).
3. If the user chooses "Add product":
   - The program asks for the product name, price, and quantity.
   - The input is validated using a try-except block.
   - The product is stored as a dictionary inside a list.

4. If the user selects "Open inventory":
   - The program displays all stored products in a clear format.
   - If there are no products, a message is shown.

5. If the user selects "See calculations":
   - The program calculates:
     - Total number of products
     - Total inventory value (price × quantity)

6. The program runs continuously until the user selects "Exit".

## Status

> The program is currently a basic interactive console application.  
> It demonstrates how Python manages inventory data using lists and dictionaries,
 along with input validation and simple calculations.