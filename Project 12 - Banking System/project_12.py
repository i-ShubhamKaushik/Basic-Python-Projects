# PROJECT 12 - BANKING SYSTEM

# Creating accounts
# Login
# Deposits
# Withdrawals
# Balance validation
# Money transfer
# Transaction history


accounts= {}

def get_input(field):
    return input(f"Enter {field}: ")

def next_line():
    print("\n")

def create_acc():
    next_line()
    account_no= get_input("Account Number")
    if account_no in accounts:
        print("\nAccount number already exists..!\n")
    else:
        next_line()
        name= get_input("Name")
        age= int(get_input("Age"))
        if age<18:
            print("\nYou must be 18 to create a bank account!\n")
        else:
            phone_num= (get_input("Phone Number"))
            if len(phone_num)<10 or len(phone_num)>10:
                print("\nPhone number must have only 10 digits...!\n")
            else:
                initial_bal= float(get_input("Initial Balance"))
                user_input= input(
                    "\n - - Account Type - -"
                    "\n1. Savings"
                    "\n2. Current"
                    "\n\n:"
                )
                if user_input=="1":
                    account_type= "Savings"
                elif user_input=="2":
                    account_type= "Current"
                else:
                    print("\nInvalid Argument..!\n")
        account_pin= (get_input("New Pin"))
        confirm_pin= get_input("PIN again to confirm")
        if account_pin!=confirm_pin:
            print("\nPIN didn't match, Try Again\n")
        else:
            accounts.update({account_no : {
                "name" : name,
                "age" : age,
                "Phone Number" : phone_num,
                "Balance" : initial_bal,
                "Account Type" : account_type,
                "Account Pin" : account_pin,
            }})
            print(f"Congratulations.. {accounts[account_no]["name"]}")
            print("Your Account created successfully...!\n----------\n")

            for acc_no, details in accounts.items():
                print(f"\nAccount No. : {acc_no}")
                for key, value in details.items():
                    print(f"{key} : {value}")

def login():
    next_line()
    account_no= get_input("Account Number")
    if account_no not in accounts:
        print(f"\nAccount number: '{account_no}' does not exist\n")
    else:
        next_line()
        password= get_input("Your PIN")
        if password== accounts[account_no]["Account Pin"]:
            print("\nLogged in Successfully\n")
        else:
            print("\nIncorrect Password\n")


def balance():
    pass

def transactions():
    pass


def main_menu():
    while True:
        user_input= input(
            "\n - - Main MENU - - "
            "\n1. Create account"
            "\n2. Login "
            "\n3. Exit"
            "\n4. Help & Support"
            "\n\n:"
        )
        if user_input=="1":
            create_acc()
        elif user_input=="2":
            login()
        elif user_input=="3":
            print("\nGood Bye..!\n")
            break
        else:
            print("\nInvalid Argument..!\n")


main_menu()