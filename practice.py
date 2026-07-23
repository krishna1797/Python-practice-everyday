import pickle
import os

FILENAME = "contacts.dat"

def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "rb") as f:
            return pickle.load(f)
    return {}

def save_contacts(contacts):
    with open(FILENAME, "wb") as f:
        pickle.dump(contacts, f)

contacts = load_contacts()

while True:
    print("\n====== CONTACT BOOK ======")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter name: ").strip()
        if name in contacts:
            print("Contact already exists!")
        else:
            phone = input("Enter phone number: ")
            contacts[name] = phone
            save_contacts(contacts)
            print("Contact added successfully!")

    elif choice == "2":
        if len(contacts) == 0:
            print("No contacts found.")
        else:
            print("\n----- CONTACTS -----")
            for name, phone in contacts.items():
                print(f"{name} : {phone}")

    elif choice == "3":
        name = input("Enter name to search: ").strip()
        if name in contacts:
            print(f"{name}'s Phone Number: {contacts[name]}")
        else:
            print("Contact not found.")

    elif choice == "4":
        name = input("Enter name to update: ").strip()
        if name in contacts:
            new_phone = input("Enter new phone number: ")
            contacts[name] = new_phone
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    elif choice == "5":
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Contact not found.")

    elif choice == "6":
        print("Thank you for using Contact Book!")
        break




