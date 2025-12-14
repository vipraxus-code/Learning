sandwich_orders = ["Pastrami", "American sub", "Ayvalik toast", "Pastrami", "Bacon", "Bacon, Egg and cheese", "Pastrami", "Bagel toast"]

print('\nWelcome to Subway! Unfortunately, we ran out of "Pastrami". Please order something else.\n')
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

finished_sandwiches = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"Cooking: {current_sandwich}!")
    finished_sandwiches.append(current_sandwich)

print("\n" + ", ".join(finished_sandwiches) + ".", "\n")