# Users
class User:
    """A class representing a user."""

    def __init__(self, first_name, last_name, **info):
        """Initialise typical user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        for key, value in info.items():
            setattr(self, key, value)

    def describe_user(self):
        """Print a summary of the user's information."""
        info = ', '.join(
            f"{key.capitalize()}: {value}"
            for key, value in self.__dict__.items()
            if key not in ['first_name', 'last_name']
        )
        print(f"User: {self.first_name} {self.last_name}, {info}")

    def greet_user(self):
        """Greet the user with a personalized message."""
        print(f"Hello, {self.first_name} {self.last_name}!")


if __name__ == "__main__":
    print("Creating instances of the User class...")
    user1 = User(
        "John",
        "Doe",
        age=30,
        location="New York",
        occupation="Engineer",
        hobbies=["reading", "cycling"],
        favorite_color="blue"
    )
    user1.describe_user()
    user1.greet_user()
    user2 = User(
        "Jane",
        "Smith",
        age=25,
        location="Los Angeles",
        occupation="Designer",
        hobbies=["painting", "traveling"],
        favorite_color="green"
    )
    user2.describe_user()
    user2.greet_user()
    user3 = User(
        "Alice",
        "Johnson",
        age=28,
        location="Chicago",
        occupation="Doctor",
        hobbies=["running", "cooking"],
        favorite_color="purple"
    )
    user3.describe_user()
    user3.greet_user()
