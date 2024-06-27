# Project 1: Contact Book
# Description: Create a contact book where users can add, remove, view, and search for contacts

# Hints and Clues:
# Create a dictionary to store contacts: Use names as keys and phone numbers as values.
# Functions: Implement functions to add, remove, view, and search for contacts.
# Main Loop: Use a while loop to keep the program running until the user decides to exit.

contacts = {}

def add_contact(name, phone):
    contacts[name] = phone
    print(f"Contact {name} added.")

def remove_contact(name):
    # TODO: Check if contact exists before removing
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} removed.")
    else:
        print("Contact not found.")

def view_contacts():
    # TODO: Display all contacts in the dictionary
    if contacts:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts available.")

def search_contact(name):
    # TODO: Search for a contact by name
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def contact_book():
    while True:
        print("\n1. Add contact")
        print("2. Remove contact")
        print("3. View contacts")
        print("4. Search contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            add_contact(name, phone)
        elif choice == '2':
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif choice == '3':
            view_contacts()
        elif choice == '4':
            name = input("Enter name to search: ")
            search_contact(name)
        elif choice == '5':
            print("Exiting contact book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

contact_book()