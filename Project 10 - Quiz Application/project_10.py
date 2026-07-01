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

def admin():
    admin = input("\nEnter your admin code: ")
    if admin == "admin@12":
        print("\n\nStatus : You now have admin access...!")
        while True:
            admin_input= input("\n     M E N U     \nPress '1' to add Question \nPress '2' log out \n\n:")
            if admin_input=="1":
                new_question= input("\nInput new question: ")
                option_a = input("\noption 'a' : ")
                option_b = input("option 'b' : ")
                option_c = input("option 'c' : ")
                option_d = input("option 'd' : ")
                answer = input("\nCorrect option: ").lower()
                questions.append({"question" : new_question, "options" : {"a" : option_a, "b" : option_b, "c" : option_c, "d" : option_d}, "answer" : answer})
                print("\nQuestion added successfully...!\n")
            elif admin_input=="2":
                print("\n\nStatus : Logged out as admin")
                break
            else:
                print("\nChoice should be from MENU\n")
    else:
        print("\nIncorrect code\n")


# MENU SECTION

while True:
    user_input= input("\n     M E N U     \nPress '1' to start Quiz \nPress '2' to view score \nPress '3' to Exit \nPress '4' to login as Admin \n\n:")

    if user_input=="1":
        quiz()
    elif user_input=="2":
        previous_score()
    elif user_input=="3":
        print(f"\nGood bye... {name}!\n")
        break
    elif user_input=="4":
        admin()
    else:
        print("\nInvalid Argument..!")