# PROJECT 8 - PASSWORD GENERATOR

import random

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*"
password = ""

n = int(input("\nEnter length for your password: "))

if n<=0 :
    print("\nLength must be positive..!\n")
else:
    for i in range(n):
        password+= random.choice(chars)
    print(f"\nGenerated Password : {password}\n")