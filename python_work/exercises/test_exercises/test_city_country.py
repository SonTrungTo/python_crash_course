from exercises.city_country import city_country

def test_city_country_name():
    """Test if "Santiago, Chile" is formatted correctly."""
    city_country_name = city_country("santiago", "chile")
    assert city_country_name == "Santiago, Chile"
