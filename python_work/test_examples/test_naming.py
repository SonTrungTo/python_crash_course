from naming import get_formatted_name

def test_first_last_name():
    """Test if "John Doe" is formatted correctly."""
    formatted_name = get_formatted_name("john", "doe")
    assert formatted_name == "John Doe"
