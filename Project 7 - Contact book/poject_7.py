# PROJECT 7 - CONTACT BOOK

contacts = {}

def add_contact():
    x = input("\nEnter contact name: ")
    
    if x in contacts:
        print(f"\n'{x}' is already in your contacts!\n")
    else:
        y = input("\nEnter Contact number: ")
        if len(y) != 10 or not y.isdigit():
            print("\nPhone number must contain exactly 10 digits!\n")
        else:
            contacts[x] = y
            print("\nContact added successfully!\n")

def search_contact():
    x = input("\nEnter name: ")
    if x in contacts:
        print(f"Contact number of {x} is: {contacts[x]}\n")
    else:
        print("\nContact is not saved!\n")

def del_contact():
    x =  input("\nEnter name of the contact you want to delete: ")
    if x in contacts:
        contacts.pop(x, None)
        print("\nContact deleted successfully!\n")
    else:
        print("\nThis contact is not saved!\n")

def view_contacts():
    if contacts == {}:
        print("\nNo contacts added yet!\n")
    else:
        for name, number in contacts.items():
            print(f"\n{name} : {number}")

while True:
    menu = input("\tM E N U  \nPress '1' to Add New Contact \nPress '2' to see Your Contacts \nPress '3' to Search a Contact \nPress '4' to Delete a contact \nPress '5' to Exit!  : ")

    if menu=="1":
        add_contact()
    elif menu=="2":
        view_contacts()
    elif menu=="3":
        search_contact()
    elif menu=="4":
        del_contact()
    elif menu=="5":
        print("\nGood Bye...!\n")
        break
    else:
        print("\nInvalid Arguement...!\n")