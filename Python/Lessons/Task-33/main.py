countries_and_rivers = {
    "egypt": "nile",
    "amazon": "brazil",
    "danube": "germany"
}
for country, river in countries_and_rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")
print("Countries mentioned:")
for country in countries_and_rivers.keys():
    print(f"\t{country.title()}")
print("Rivers mentioned:")
for river in countries_and_rivers.values():
    print(f"\t{river.title()}")