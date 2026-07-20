# Restaurant
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print a description of the restaurant."""
        print(f"{self.restaurant_name} serves {self.cuisine_type} cuisine.")

    def open_restaurant(self):
        """Print a message indicating that the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")


if __name__ == "__main__":
    print("Creating an instance of the Restaurant class...")
    restaurant = Restaurant("Sakura", "Japanese")
    print(f"Restaurant name attribute: {restaurant.restaurant_name}")
    print(f"Cuisine type attribute: {restaurant.cuisine_type}")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()
