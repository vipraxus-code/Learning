guests = ["john smith", "alan walker", "diana rachel", "peter parker"]
for guest in guests:
    print(f"Hello {guest.title()}, you`re invited to the party!")
cant_come = guests.pop(0)
new_guest = "tony stark"
print(f"\nSeems like {cant_come.title()} can`t come to the party, lets replace his letter. New guest is {new_guest.title()}!\n")
guests.append(new_guest)
print(f"Hello {new_guest.title()}, you`re invited to the party!")
print("\nOh, I just got a new table! We can invite 3 more guests!\n")
new_guests = ["alexander thompson", "sophia rodriguez", "marcus chen"]
for guest in new_guests:
    guests.append(guest)
for guest in new_guests:
    print(f"Hello {guest.title()}, you`re invited to the party!")
print("\nUnfortunately, the table won`t arrive on time, so we have sits only for 2 guests.\n")
for _ in range(5):
    removed_guest = guests.pop()
    print(f"Sorry {removed_guest.title()}, we have sits only for 2 persons, the letter that was sent earlier isn`t valid now.")
print(f"\nFinal guests list has {len(guests)} guests: {', '.join(guest.title() for guest in guests)}\n")