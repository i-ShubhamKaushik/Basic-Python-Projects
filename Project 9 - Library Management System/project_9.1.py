# PROJECT 9 - LIBRARY MANAGEMENT SYSTEM

name=input("Enter name: ")
print(f"\nWelcome to the library, {name}\n")

books = {
    "harry potter" : "available",
    "death note" : "available",
    "marvels" : "issued",
}

def new_book():
    x = input("\nEnter name of the book: ").lower()
    if  x in books:
        print(f"\n'{x}' is already available..!\n")
    else:
        y = "available"
        books[x]=y
        print(f"\n'{x}' added successfully!\n")

def book_issued():
    x = input("\nEnter book name: ").lower()
    if x not in books:
        print("\nBook not found..!\n")
    elif books[x]=="available":
        books[x]="issued"
        print(f"\n'{x}' issued successfully!\n")
    elif books[x]=="issued":
        print(f"\n{x} is already issued..!\n")
    
def book_return():
    x = input("\nEnter book name: ").lower()
    if x not in books:
        print("\nBook not found..!\n")
    elif books[x]=="issued":
        books[x]="available"
        print(f"\n'{x}' is now available!\n")
    else:
        print(f"\n'{x}' is not issued...!\n")

def show_books():
    for name,status in books.items():
        print(f"\n{name} : {status}")
    print("\n")

def available_book():
    for name, status in books.items():
        if status == "available":
            print(f"\n{name}")
    print("\n")

def search_book():
    x = input("\nEnter name of the book: ").lower()
    if x not in books:
        print("\nBook not found...!\n")
    else:
        for name, status in books.items():
            if name == x:
                print(f"\n{name} : {status}\n")

def remove_book():
    x = input("\nEnter book name: ").lower()
    if x not in books:
        print("\nBook not found...!\n")
    else:
        books.pop(x)
        print(f"\n'{x}' removed successfully..!\n")

while True:
    user_input= input("\tM E N U  \nPress '1' to Add New Book \nPress '2' to issue a book \nPress '3' to return a book \nPress '4' to show available books \nPress '5' to see all books data \nPress '6' to search a book \nPress '7' to remove a book \nPress '8' to Exit!  : ")

    if user_input=="1":
        new_book()
    elif user_input=="2":
        book_issued()
    elif user_input=="3":
        book_return()
    elif user_input=="4":
        available_book()
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