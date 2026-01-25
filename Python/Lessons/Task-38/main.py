users_favorite_numbers = {
    "james": 12,
    "emily": [30, 11, 69],
    "william": 5,
    "olivia": 22,
    "noah": [7, 67],
    }

for user, answer in users_favorite_numbers.items():
    if type(answer) == int:
        print(f"{user.title()}'s favorite number is {answer}.")
    else:
        print(f"{user.title()}'s favorite numbers is {', '.join(str(number) for number in answer)}.")

