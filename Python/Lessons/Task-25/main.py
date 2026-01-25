for i in range(100):
    age = i
    if age < 2:
        print("Toddler")
    elif age < 4:
        print("Baby")
    elif age < 13:
        print("Kid")
    elif age < 20:
        print("Teen")
    elif age < 65:
        print("Adult")
    elif age >= 65:
        print("Elderly person")
    else:
        print("Error")