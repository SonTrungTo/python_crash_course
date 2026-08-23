def city_country(
        city: str,
        country: str,
        population: str = ""
    ) -> str:
    """Return a string in the format 'City, Country'."""
    if population:
        city_country_name = f"{city.title()}, {country.title()} - Population: {population}"
    else:
        city_country_name = f"{city.title()}, {country.title()}"
    return city_country_name
