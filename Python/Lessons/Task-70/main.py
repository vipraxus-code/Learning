print("Enter two numbers and this programm will print the sum.")
while True:
    try:
        number1 = float(input("Enter first: "))
        break
    except ValueError:
        print("You must enter a number!", end=" ")
while True:
    try:
        number2 = float(input("Enter second: "))
        break
    except ValueError:
        print("You must enter a number!", end=" ")
print(f"Answer: {number1 + number2}")