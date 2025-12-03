# Database
users = {
    "user_1": {
        "first_name": "Elena",
        "last_name": "Rodriguez",
        "age": "18",
        "city": "Portland",
    },
    "user_2": {
        "first_name": "John",
        "last_name": "Smith",
        "age": "25",
        "city": "Boston",
    },
    "user_3": {
        "first_name": "Marcus",
        "last_name": "Chen",
        "age": "42",
        "city": "Austin",
    },
}

# Info printing
for user, information in users.items(): 
    print(user)
    for key, value in information.items():
        if key == "first_name":
            print(f"    First name: {value}")
        elif key == "last_name":
            print(f"    Last name: {value}")
        elif key == "age":
            print(f"    Age: {value}")
        elif key == "city":
            print(f"    City: {value}")
        else:
            print("Unknown error")