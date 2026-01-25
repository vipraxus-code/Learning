people_and_places = {}

while True:
    name = input("Enter your name: ")
    place = input("If you could visit any place on earth, where would it be?: ")
    people_and_places[name] = place
    if input("Continue the poll? (Yes/No): ") == "Yes":
        continue
    else:
        break

print("\n --- POLL RESULTS --- ")
for person, place in people_and_places.items():
    print(f"{person} wood like to visit {place}.")