# PROJECT 11 - STUDENT MANAGEMENT SYSTEM

students = {
    "101": {
        "name": "Shubham",
        "age": 18,
        "course": "B.Tech CSE",
        "semester": 1,
        "cgpa": 8.5
    },

    "102": {
        "name": "Rahul",
        "age": 19,
        "course": "B.Tech CSE",
        "semester": 2,
        "cgpa": 8.1
    }
}


def get_input(field):
    return input(f"Enter {field}: ")

def next_line():
    print("\n")


def add_student():
    next_line()
    roll_no = get_input("Roll No")
    if roll_no in students:
        print(f"\n{roll_no} is already present!\n")
    else:
        next_line()
        name = get_input("Name")
        age = int(get_input("Age"))
        course = get_input("Course")
        semester = int(get_input("Semester"))
        cgpa = float(get_input("CGPA"))
        students.update({roll_no : {
            "name" : name,
            "age" : age,
            "course" : course,
            "semester" : semester,
            "cgpa" : cgpa
        }})
        print("\nStudent added successfully!\n")
    

def search_student():
    next_line()
    roll_no= get_input("Roll No")
    if roll_no not in students:
        print("\nStudent not found...!\n")
    else:
        print("\n")
        for key, value in students[roll_no].items():
            print(f"{key} : {value}")
        next_line()


def update_student():
    next_line()
    roll_no= get_input("Roll No")
    if roll_no not in students:
        print("\nStudent not found...!\n")
    else:
        while True:
            user_input= input(
                "\n1. Name"
                "\n2. Age"
                "\n3. Course"
                "\n4. Semester"
                "\n5. CGPA"
                "\n6. Cancel Update"
                "\n\n:"
            )

            if user_input=="1":
                next_line()
                name= get_input("New Name")
                students[roll_no]["name"] = name
                print("\nName Updated Successfully!\n")
                break
            elif user_input=="2":
                next_line()
                age= int(get_input("New Age"))
                students[roll_no]["age"] = age
                print("\nAge Updated Successfully!\n")
                break
            elif user_input=="3":
                next_line()
                course= get_input("New Course")
                students[roll_no]["course"] = course
                print("\nCourse Updated Successfully!\n")
                break
            elif user_input=="4":
                next_line()
                semester= int(get_input("New Semester"))
                students[roll_no]["semester"] = semester
                print("\nSemester Updated Successfully!\n")
                break
            elif user_input=="5":
                next_line()
                cgpa= float(get_input("New CGPA"))
                students[roll_no]["cgpa"] = cgpa
                print("\nCGPA Updated Successfully!\n")
                break
            elif user_input=="6":
                print("\nUpdate Cancelled..!\n")
                break
            else:
                print("\nInvalid Argument..!")



def delete_student():
    next_line()
    roll_no= get_input("Roll No")
    if roll_no not in students:
        print("\nStudent not found...!\n")
    else:
        print(f"\nAre you sure you want to delete '{students[roll_no]['name']}'")
        while True:
            user_input= input(
                "Press 'Y' for Yes"
                "\nPress 'N' for No"
                "\n\n:"
            ).lower()
            if user_input=="y":
                del students[roll_no]
                print("\nDeleted successfully..!\n")
                break
            elif user_input=="n":
                print("\nDeletion Cancellled..!\n")
                break
            else:
                print("\nInvalid Argument..! (Only Yes and No accepted)\n")


def show_all():
    next_line()
    for rollno, details in students.items():
        print(f"Roll no : {rollno}")
        for key, value in details.items():
            print(f"{key} : {value}")
        print("\n------------------\n")



while True:
    user_choice= input(
        "\n-- STUDENT MANAGEMENT SYSTEM --"
        "\n1. Add Student"
        "\n2. Search Student"
        "\n3. Update Student"
        "\n4. Delete Student"
        "\n5. Show All Students"
        "\n6. Exit"
        "\n\n:"
    )

    if user_choice=="1":
        add_student()
    elif user_choice=="2":
        search_student()
    elif user_choice=="3":
        update_student()
    elif user_choice=="4":
        delete_student()
    elif user_choice=="5":
        show_all()
    elif user_choice=="6":
        print("\nGood Bye!\n")
        break
    else:
        print("\nERROR : Invalid Argument...!\n")