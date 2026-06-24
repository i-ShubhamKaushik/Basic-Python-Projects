# PROJECT 6 - TO DO LIST

tasks_list = []

menu = {
    1 : "Show Task",
    2 : "Add task",
    3 : "Remove task"
}

def show_tasks():
    for i, task in enumerate(tasks_list, start=1):
        print(f"\n{i}. {task}")

def removetask(n):
    if 1 <= n <= len(tasks_list):
        removed = tasks_list.pop(n - 1)
        return removed
    else:
        print("\nInvalid task number\n")


while True:
    user_input = input("\tM E N U  \nPress '1' to Add New Tasks \nPress '2' to see Your Tasks \nPress '3' to Remove Tasks \nPress '4' to Exit!  :")
    if user_input=="1":
        x = input("\nEnter task: \n")
        tasks_list.append(x)
    elif user_input=="2":
        if tasks_list == []:
            print("\nNo tasks added yet..!\n")
        else:
            show_tasks()
    elif user_input=="3":
        n = int(input("\nEnter task no. you want to delete: \n"))
        removed = removetask(n)
        if removed is not None:
            print(f"\nRemoved : {removed}\n")
    elif user_input=="4":
        print("\nGood Bye..!\n")
        break
    else:
        print("\nInvalid Choice...\n")