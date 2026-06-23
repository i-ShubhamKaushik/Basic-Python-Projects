# PROJECT 3 – THE PERFECT GUESS

# We are going to write a program that generates a random number and asks the user to 
# guess it. 
# If the player’s guess is higher than the actual number, the program displays “Lower 
# number please”. Similarly, if the user’s guess is too low, the program prints “higher 
# number please” When the user guesses the correct number, the program displays the 
# number of guesses the player used to arrive at the number. 
# Hint: Use the random module.

import random

number = random.randint(1,100)
guesses = 0

while True:
    user_guess = int(input("Enter number: "))
    guesses +=1

    if (user_guess==number):
        print(f"You have gueesed the number: {number} in '{guesses}' attempts..!")
        break
    elif user_guess>number:
        print("Lower number, Please!")
    elif user_guess<number:
        print("Higher number, Please!") 