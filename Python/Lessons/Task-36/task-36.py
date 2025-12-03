# Database
pets = [
    {"type": "dog", "owner": "alice"},
    {"type": "cat", "owner": "john"},
    {"type": "parrot", "owner": "marcus"},
    {"type": "capybara", "owner": "elena"},
    {"type": "turtle", "owner": "austin"},
]

# Info printing
for pet_number, pet in enumerate(pets, start=1):
    print(f"Pet #{pet_number}:")
    for key, value in pet.items():
        print(f"    {key.title()}: {value.title()}")