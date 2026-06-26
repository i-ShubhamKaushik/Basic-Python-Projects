import random

length = int(input("\nLength of password you want?: "))
asking = input("\nDo you want symbols and numbers in passwords? (Yes or No): ").lower()

password = ""

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
alphabets= "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"

if length >=1:
    if asking == "yes":
        for i in range(length):
            password+=random.choice(chars)
        print(f"\nGenerated Password : {password}\n")
    elif asking == "no":
        for i in range(length):
            password+=random.choice(alphabets)
        print(f"\nGenerated Password : {password}\n")
    else:
        print("\nChoice must be (Yes or No)\n")
elif length==0:
    print("\nLength cannot be zero")
else:
    print("\nLength should be a positive number")