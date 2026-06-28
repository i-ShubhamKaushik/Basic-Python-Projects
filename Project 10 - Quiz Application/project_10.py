# PROJECT 10 - QUIZ APPLICATION

import random

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

    print(f"\nFinal Score: {score}/{len(questions)}")

quiz()