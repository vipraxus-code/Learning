def get_city_info(city, country, population=""):
    if population:
        return f"{city.title()}, {country.title()}; Population - {population}."
    else:
        return f"{city.title()}, {country.title()}."