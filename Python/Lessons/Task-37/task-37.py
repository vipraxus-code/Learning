# Database
favorite_places = {
    "Silverpine Valley": ["john", "elena"],
    "Marble Coast": ["chen", "austin", "marcus"],
    "Redstone Springs": ["eggsy"],
}

# Info printing
for place, people in favorite_places.items():
    print(f"{place} is loved by {', '.join(person.title() for person in people)}")