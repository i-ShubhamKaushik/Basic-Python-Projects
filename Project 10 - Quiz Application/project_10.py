# PROJECT 10 - QUIZ APPLICATION

import random

name = input("\nEnter your name: ")
print(f"\nWelcome, {name}!")

questions = [
    {
        "question" : "Which keyword is used to define a function?",
        "options" : {
            "a" : "func",
            "b" : "define",
            "c" : "def",
            "d" : "function",
        },
        "answer" : "c"
    },

    {
        "question" : "Which data type is mutable?",
        "options" : {
            "a" : "tuple",
            "b" : "list",
            "c" : "string",
            "d" : "int",
        },
        "answer" : "b"
    },

    {
        "question" : "How we display an empty set?",
        "options" : {
            "a" : "{}",
            "b" : "set{}",
            "c" : "set()",
            "d" : "[]",
        },
        "answer" : "c"
    },

    {
        "question" : "Which anime has more than thousand episodes?",
        "options" : {
            "a" : "Naruto",
            "b" : "One Piece",
            "c" : "Bleach",
            "d" : "Demon Slayer"
        },
        "answer" : "b"
    },

]

def quiz():
    print("----  Quiz Started  ----")
    score = 0
    random.shuffle(questions)

    for question in questions:
        print("\n")
        print(question["question"])
        print("\n")

        for key, value in question["options"].items():
            print(f"{key} : {value}")
        answer = input("\nEnter your answer: ").lower()
        
        if answer == question["answer"]:
            print("\nCorrect answer")
            score+=1
        else:
            print("\nIncorrect answer")

    print(f"\nFinal Score: {score}/{len(questions)}\n")
    
    with open("Project 10 - Quiz Application/previous_score.txt", "w") as f:
        f.write(f"Your previous score is : {score}/{len(questions)}")


def previous_score():
    with open("Project 10 - Quiz Application/previous_score.txt", "r") as f:
        score=f.read()
        print(f"\n{score}\n")

# MENU SECTION

while True:
    user_input= input("\n     M E N U     \nPress '1' to start Quiz \nPress '2' to add question \nPress '3' to view score \nPress '4' to Exit \n\n:")

    if user_input=="1":
        quiz()
    elif user_input=="2":
        pass
    elif user_input=="3":
        previous_score()
    elif user_input=="4":
        print(f"\nGood bye... {name}!\n")
        break
    else:
        print("\nInvalid Argument..!")