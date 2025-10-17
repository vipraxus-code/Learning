users = ["lora", "ben", "admin", "john", "sora"]

if users == []:
        print("User list is empty.")
elif users != []:
    for user in users: 
        if user == "admin":
            print("Hello, Admin, want to see how deals going?")
        elif user != "admin":
            print(f"Hello, {user.title()}, thanks for using our service!")
        else:
            print("Error")
else:
    print("Error")