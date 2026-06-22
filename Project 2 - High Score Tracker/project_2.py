# Project 2 - High Score Tracker

# The game() function in a program lets a user play a game and returns the score 
# as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or 
# contains the previous Hi-score. You need to write a program to update the Hi
# score whenever the game() function breaks the Hi-score. 

import random
def game():
    print("You are now playing the game>>")
    score = random.randint(1,101)

    with open("Project 2 - High Score Tracker/hi-score.txt", "r") as f:
        hiscore = f.read()

        if hiscore != "":
            hiscore = int(hiscore)
        else:
            hiscore = 0

        print(f"our score: {score}")
        if (score > hiscore):
            with open("Project 2 - High Score Tracker/hi-score.txt", "w") as f:
                f.write(f"Your high score is: {str(score)}")

        return score

game()