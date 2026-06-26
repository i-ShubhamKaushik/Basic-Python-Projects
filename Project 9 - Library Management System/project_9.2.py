# Improved version of 'PROJECT 9' by using nested dictionaries

name = input("\nEnter name: ")
print(f"\nWelcome to the library, {name}\n")

books= {
    "death note" : {
        "status" : "available",
        "issued_to" : "none",
    },
    "harry potter" : {
        "status" : "issued",
        "issued_to" : "harry"
    }
}

def add_books():
    book_name = input("\nBook Name: ").lower()
    if book_name in books:
        print("\nBook already exist!\n")
    else:
        books.update({book_name : {"status" : "available", "issued_to" : "none"}})
        print(f"\n'{book_name}' added successfully..!\n")

def issue_books():
    book_name= input("\nBook Name: ").lower()
    if book_name not in books:
        print("\nBook not found..!\n")
    else:
        if books[book_name]["status"]=="available":
            books[book_name]["status"]="issued"
            name= input(f"\nIssuing '{book_name}' to: ")
            books[book_name]["issued_to"]=name
            print(f"\'{book_name}' successfully issued to '{name}'\n")
        else:
            print("\nBook is not available\n")

def return_book():
    book_name= input("\nBook Name: ").lower()
    if book_name not in books:
        print("\nBook not found..!\n")
    else:
        if books[book_name]["status"]=="issued":
            books[book_name]["status"]="available"
            books[book_name]["issued_to"]="none"
            print(f"\n'{book_name}' is returned to library..!\n")
        else:
            print("\nBook is not issued..!\n")

def show_books():
    for name,  info in books.items():
        print(f"\n----{name.upper()}----")
        for status, mark in info.items():
            print(f"\n{status} : {mark}")
        print("\n")

def search_book():
    book_name= input("\nBook name: ").lower()
    if book_name not in books:
        print("\nBook not found..!\n")
    else:
        for name, info in books.items():
            if name == book_name:
                print(f"\n----{name.upper()}----")
                for status, mark in info.items():
                    print(f"\n{status} : {mark}")
        print("\n")            

def remove_book():
    book_name = input("\nBook name: ").lower()
    if book_name not in books:
        print("\nBook not found..!")
    else:
        books.pop(book_name)
        print(f"\n'{book_name}' is removed..!\n")

def available_books():
    print("\n   Available Books")
    for name in books:
        if books[name]["status"]=="available":
            print(f"\n{name}")
    print("\n")

while True:
    user_input= input("\tM E N U  \nPress '1' to Add New Book \nPress '2' to issue a book \nPress '3' to return a book \nPress '4' to show available books \nPress '5' to see all books data \nPress '6' to search a book \nPress '7' to remove a book \nPress '8' to Exit!  : ")

    if user_input=="1":
        add_books()
    elif user_input=="2":
        issue_books()
    elif user_input=="3":
        return_book()
    elif user_input=="4":
        available_books()
    elif user_input=="5":
        show_books()
    elif user_input=="6":
        search_book()
    elif user_input=="7":
        remove_book()
    elif user_input=="8":
        print(f"\nGood bye...!, {name}\n")
        break
    else:
        print("\nInvalid argument..!\n")