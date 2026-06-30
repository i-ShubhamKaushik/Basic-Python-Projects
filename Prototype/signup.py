account = [
    {
        "username" : "xyz",
        "details" : {
            "name" : "xyz",
            "surname" : "xyz",
            "dob" : "xyzdate",
            "password" : "xyz",
        }
    }
]


while True:
    name = input("\nEnter name: ")
    surname = input("\nEnter surname: ")
    username = input("\nSet username: ")
    dob = input("\nenter date of birth: ")
    password = input("\nSet password: ")

    for info in account:
        info["details"]["name"] = name
        info["details"]["surname"] = surname
        info["details"]["dob"] = dob
        info["username"] = username
        info["details"]["password"] = password
    break

