# City names
def city_country(city: str, country: str) -> str:
    """Return a string of the form 'City, Country'."""
    return f"{city.title()}, {country.title()}"

print(city_country('santiago', 'chile'))
print(city_country('paris', 'france'))
print(city_country('tokyo', 'japan'))
