class Privileges:
    """A class to represent a user's privileges."""

    def __init__(self):
        """Initialize the privileges."""
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            ]

    def show_privileges(self):
        """Display the privileges."""
        print("Privileges:")
        for privilege in self.privileges:
            print(f"- {privilege}")
