cities = {
    "los_angeles": {
        "country": "USA",
        "capital": "No",
        "population": "3880000",
        "fact": "Second-most populous city in the United States and the commercial and cultural hub of Southern California."
    },
    "Tokyo": {
        "country": "Japan",
        "capital": "Yes",
        "population": "41000000",
        "fact": "Tokyo is the world's most populous metropolitan area, with a population of over 37 million, and was formerly known as Edo."
    },
    "London": {
        "country": "Great Britain",
        "population": "8950000",
        "capital": "Yes",
        "fact": "London is the capital of England and the UK, has been a major settlement for nearly 2,000 years, and is home to over 300 languages."
    }
}

for city, info in cities.items():
    print(f"\n{city.title()}:")
    for key, value in info.items():
        print(f"    {key.title()}: {value}")