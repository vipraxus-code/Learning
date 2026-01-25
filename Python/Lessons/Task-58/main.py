def made_sandwich(*toppings):
    print("Making sandwich with folliwing toppings:")
    for topping in toppings:
        print(f"- {topping}")

made_sandwich("tomato", "cucumber", "bread")