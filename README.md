# Inventory Management System (CSV Persistence)

## Description

Console-based inventory system developed in Python.
Supports CRUD operations, statistics, and CSV persistence to store data between sessions.

---

## Project Structure

```
project/
├── main.py
├── menu.py
├── services/inventory_services.py
├── utils/file_handler.py
├── data/inventory.csv
```

---

## Features

* Add, view, search, update, and delete products
* Calculate:

  * Total units
  * Total value
  * Most expensive product
  * Highest stock product
* Save and load inventory using CSV
* Merge or overwrite data when loading
* Input validation and error handling

---

## Data Structure

```
{
    "name": str,
    "price": float,
    "quantity": int
}
```

---

## Usage

Run the program:

```
python main.py
```

Menu options:

```
1. Add product
2. Show inventory
3. Search product
4. Update product
5. Delete product
6. Calculate statistics
7. Save CSV
8. Load CSV
9. Exit
```

---

## CSV Format

```
name,price,quantity
Laptop,1200.50,5
Mouse,25.99,10
```

Rules:

* Header must match exactly
* Price ≥ 0, Quantity ≥ 0
* Invalid rows are skipped

---

## Merge Policy

* Existing product → quantity is added, price updated
* New product → added to inventory

---

## Error Handling

Handles invalid input, file errors, and corrupted data without stopping the program.

