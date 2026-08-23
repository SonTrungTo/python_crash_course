def city_country(city: str, country: str) -> str:
    """Return a string in the format 'City, Country'."""
    city_country_name = f"{city.title()}, {country.title()}"
    return city_country_name
