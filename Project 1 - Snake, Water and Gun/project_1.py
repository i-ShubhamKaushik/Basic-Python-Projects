# PROJECT 1: SNAKE, WATER, GUN GAME 

# We all have played snake, water gun game in our childhood. If you haven’t, google the rules of this game and write a python program capable of playing this game with the user. 


import random

choices = {
    "s" : "snake",
    "w" : "water",
    "g" : "gun",
}

computer = random.choice(["s", "g", "w"])
user = input("Enter your choice (s for Snake, w for Water, g for Gun): ").lower()

if user == computer:
    print("It's a Draw..!")

elif (
    (user == "s" and computer == "w") or
    (user == "w" and computer == "g") or
    (user == "g" and computer == "s")
):
    print("You Win ....!")

else:
    print("Computer wins")