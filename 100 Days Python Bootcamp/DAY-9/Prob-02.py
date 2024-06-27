# Project 2: Inventory Management System
# Description: Create an inventory management system for a store. Users can add, remove, and view items in the inventory.

# Hints and Clues:
# Use a dictionary to store items: Use item names as keys and quantities as values.
# Functions: Implement functions to add items, remove items, and view the inventory.
# Main Loop: Use a while loop to keep the program running until the user decides to exit.

inventory = {}

def add_item(inventory, item, quantity, price):
    if item in inventory:
        inventory[item]['quantity'] += quantity
        inventory[item]['price'] = price  # update price if necessary
    else:
        inventory[item] = {'quantity': quantity, 'price': price}
    total_price = quantity * price
    print(f"{quantity} {item}(s) added to inventory.")
    print(f"Total price of these items: ${total_price}")

def remove_item(inventory, item, remove):
    if item in inventory:
        if inventory[item]['quantity'] >= remove:
            inventory[item]['quantity'] -= remove
            if inventory[item]['quantity'] == 0:
                del inventory[item]  # remove item completely if quantity is 0
            print(f"{remove} {item}(s) removed from inventory.")
        else:
            print(f"Not enough {item}(s) in inventory to remove.")
    else:
        print(f"{item} not found in inventory.")

def view_item(inventory):
    if inventory:
        for item, details in inventory.items():
            quantity = details['quantity']
            price = details['price']
            print(f"{item}: {quantity} unit(s), ${price} per unit")
    else:
        print("Inventory is empty.")

def inventory_system():
    while True:
        print("\n1. Add item")
        print("2. Remove item")
        print("3. View inventory")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: "))
            add_item(inventory, item, quantity, price)
        elif choice == '2':
            item = input("Enter item name to remove: ")
            remove = int(input("Enter quantity to remove: "))
            remove_item(inventory, item, remove)
        elif choice == '3':
            view_item(inventory)
        elif choice == '4':
            print("Exiting inventory system. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

inventory_system()
