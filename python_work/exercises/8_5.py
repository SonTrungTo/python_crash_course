# Cities
def describe_city(city, country="USA"):
    """Display a short summary about the city and its country."""
    info = f"{city} is in {country}."
    print(info)

describe_city("New York")
describe_city("Los Angeles")
describe_city("Paris", country="France")
