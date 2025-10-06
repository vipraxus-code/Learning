my_favorite_pizzas = ["Pepperoni", "Margherita", "Hawaiian", "Meat Lovers", "BBQ Chicken"]
friend_favorite_pizzas = my_favorite_pizzas[:]
my_favorite_pizzas.append("Four Cheese")
friend_favorite_pizzas.append("Buffalo")
print("\nMy favorite pizzas are: ")
for pizza in my_favorite_pizzas:
    print(pizza)
print("\nFriend`s favorite pizzas are:")
for pizza in friend_favorite_pizzas:
    print(pizza)