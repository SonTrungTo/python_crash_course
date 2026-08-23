from exercises.city_country import city_country

def test_city_country_name():
    """Test if "Santiago, Chile" is formatted correctly."""
    city_country_name = city_country("santiago", "chile")
    assert city_country_name == "Santiago, Chile"

def test_city_country_with_population():
    """Test if city, country and population are formatted correctly."""
    city_country_name = city_country("santiago", "chile", "5000000")
    assert city_country_name == "Santiago, Chile - Population: 5000000"
