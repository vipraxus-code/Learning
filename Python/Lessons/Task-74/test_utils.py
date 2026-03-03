from utils import get_city_info


def test_get_city_info_without_population():
    assert get_city_info("santiago", "chile") == "Santiago, Chile."
    assert get_city_info("saint-petersburg", "russia") == "Saint-Petersburg, Russia."
    assert get_city_info("paris", "france") == "Paris, France."

def test_get_city_info_with_population():
    assert get_city_info("santiago", "chile", 7000000) == "Santiago, Chile; Population - 7000000."
    assert get_city_info("saint-petersburg", "russia", 6400000) == "Saint-Petersburg, Russia; Population - 6400000."
    assert get_city_info("paris", "france", 11300000) == "Paris, France; Population - 11300000."
