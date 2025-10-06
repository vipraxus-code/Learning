try:
    age_user_input = int(input("Enter your age: "))
    if age_user_input >= 16:
        print("You are now allowed to use our service!")
    elif age_user_input < 16 and age_user_input > 0:
        print("You aren`t allowed to use our service yet!")
    else:
        print("Enter a valid age!")
except ValueError:
    print("Enter a number!")