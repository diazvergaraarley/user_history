# menu.py
# Handles user interaction and menu navigation

import datetime
from services.inventory_services import *
from utils.file_handler import write_csv, load_inventory_from_csv

def show_timestamp(message):
    # Prints a message with current date and time
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print(f"[{now}] {message}")

def main_menu():
    # Load inventory from CSV at start
    inventory = load_inventory_from_csv([])

    while True:
        show_timestamp("Inventory Menu Started")
        print("""
        ---- INVENTORY MENU ----
        1. Add product
        2. Show inventory
        3. Search product
        4. Update product
        5. Delete product
        6. Calculate statistics
        7. Save inventory to CSV
        8. Load inventory from CSV
        9. Exit
        """)

        try:    
            choice = input("Select an option (1-9): ").strip()

            if choice == "1":
                # Add new product
                name = input("Enter product name: ").strip()
                price = float(input("Enter product price: "))
                quantity = int(input("Enter product quantity: "))
                
                add_product(inventory, name, price, quantity)
                show_timestamp(f"Product '{name}' added.")

            elif choice == "2":
                # Display all products
                show_inventory(inventory)

            elif choice == "3":
                # Search for a product by name
                name = input("Enter product name to search: ").strip()
                product = search_product(inventory, name)
                
                if product:
                    print(f"Found: {product}")
                else:
                    print("Product not found.")

            elif choice == "4":
                # Update product info (optional fields)
                name = input("Enter product name to update: ").strip()
                new_price = input("New price (leave blank to skip): ").strip()
                new_quantity = input("New quantity (leave blank to skip): ").strip()
                
                update_product(
                    inventory, 
                    name, 
                    new_price=float(new_price) if new_price else None,
                    new_quantity=int(new_quantity) if new_quantity else None
                )

            elif choice == "5":
                # Delete a product
                name = input("Enter product name to delete: ").strip()
                delete_product(inventory, name)

            elif choice == "6":
                # Calculate inventory statistics
                stats = calculate_stats(inventory)
                
                if stats:
                    print(f"""
                    Total units: {stats['total_units']}
                    Total value: {stats['total_value']}
                    Most expensive: {stats['most_expensive']}
                    Highest stock: {stats['highest_stock']}
                    """)
                else:
                    print("No products in inventory to calculate statistics.")

            elif choice == "7":
                # Save inventory to CSV file
                write_csv(inventory)

            elif choice == "8":
                # Load inventory from CSV file
                inventory = load_inventory_from_csv(inventory)

            elif choice == "9":
                # Exit program
                show_timestamp("Exiting Inventory Program...")
                break

            else:
                print("Invalid option. Please select a number between 1-9.")
        
        except ValueError:
            # Handles invalid numeric input
            print("Invalid option.")
            
        except Exception as e:
            # Catch unexpected errors
            print(f"Invalid option. {e}")