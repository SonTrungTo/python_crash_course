def get_formatted_name(
        first_name: str,
        last_name: str,
        middle_name: str = ""
    ) -> str:
    """Format the name to have the first letter of each word capitalized."""
    if middle_name:
        name = f"{first_name} {middle_name} {last_name}"
    else:
        name = f"{first_name} {last_name}"
    return name.title()
