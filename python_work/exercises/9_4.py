# Number served
from restaurant import Restaurant

class RestaurantWithNumberServed(Restaurant):
    """A simple attempt to model a restaurant with number served."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialise restaurant name and cuisine type attributes."""
        super().__init__(restaurant_name, cuisine_type)
        self._number_served = 0

    @property
    def number_served(self):
        """Get the number of customers served."""
        return self._number_served

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self._number_served = number
        else:
            print("Number served cannot be negative.")

    def increment_number_served(self, increment):
        """Increment the number of customers served."""
        if increment >= 0:
            self._number_served += increment
        else:
            print("Increment cannot be negative.")


if __name__ == "__main__":
    print("Creating an instance of the RestaurantWithNumberServed class...")
    restaurant = RestaurantWithNumberServed("Sakura", "Japanese")
    print(f"Restaurant name attribute: {restaurant.restaurant_name}")
    print(f"Cuisine type attribute: {restaurant.cuisine_type}")
    restaurant.describe_restaurant()
    restaurant.open_restaurant()

    # Set and increment number served
    restaurant.set_number_served(50)
    print(f"Number served: {restaurant.number_served}")
    restaurant.increment_number_served(20)
    print(f"Number served after increment: {restaurant.number_served}")
