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

def get_input(field):
    return input(f"\nEnter {field}: ")

for info in account:
    info["details"]["name"] = get_input("name")
    info["details"]["surname"] = get_input("surname")
    info["details"]["dob"] = get_input("dob")
    info["username"] = get_input("username")
    info["details"]["password"] = get_input("password")


for user in account:
    print("\n\n---- Account Info ----")
    print(f"\nUsername : {user['username']}")
    for key, value in user["details"].items():
        print(f"\n{key} : {value}")
    print("\n")