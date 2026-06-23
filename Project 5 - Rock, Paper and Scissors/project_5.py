# PROJECT 5 - ROCK, PAPER, SCISSORS 

import random

choices = {
    "r" : "rock",
    "p" : "paper",
    "s" : "scissor",
}

while True:
    computer = random.choice(["r", "p", "s"])
    user_choice= input("Enter your choice ('r' for rock, 'p' for paper, 's' for scissor): ").lower()

    if user_choice==computer:
        print(f"It's a Draw! You both have choosed: {choices[user_choice]}")

    elif (
        (user_choice=="r" and computer=="s") or
        (user_choice=="p" and computer=="r") or
        (user_choice=="s" and computer=="p")
    ):
        print(f"You Win..! \nYou : {choices[user_choice]} \t Computer : {choices[computer]}")

    else:
        print(f"Computer Wins..! \nYou : {choices[user_choice]} \t Computer : {choices[computer]}")