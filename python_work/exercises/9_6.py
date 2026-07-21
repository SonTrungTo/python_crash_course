# Ice cream stand
from restaurant import Restaurant


class IceCreamStand(Restaurant):
    """A class representing an ice cream stand."""

    def __init__(self, name, cuisine_type="ice cream", **info):
        """Initialise the ice cream stand attributes."""
        super().__init__(name, cuisine_type)
        self.flavors = info.get("flavors", [])

    def describe_restaurant(self):
        """Print a description of the ice cream stand."""
        print(f"{self.restaurant_name} serves {self.cuisine_type}.")

    def display_flavors(self):
        """Display the available ice cream flavors."""
        print(f"Available flavors at {self.restaurant_name}: {', '.join(self.flavors)}")


if __name__ == "__main__":
    # Create an instance of IceCreamStand
    ice_cream_stand = IceCreamStand(
        "Sweet Treats",
        flavors=["vanilla", "chocolate", "strawberry"]
    )

    # Describe the ice cream stand
    ice_cream_stand.describe_restaurant()

    # Display the available flavors
    ice_cream_stand.display_flavors()
