import requests


def get_country_data(country):
    url = f"https://restcountries.com/v3.1/name/{country}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()

def print_country_data(country):
    data = get_country_data(country)
    if data:
        print("-" * 50)
        print(f"Data for {country.capitalize()}:")
        print(f"\tRegion: {data[0]["subregion"]}")
        print(f"\tArea: {data[0]["area"]:,}")
        print(f"\tCapital: {data[0]["capital"][0]}")
        print(f"\tPopulation: {data[0]["population"]:,}")
        print("-" * 50)
    else:
        print("Invalid country.")

country = input("Data of which country you'd like to get? ")
print_country_data(country.lower())