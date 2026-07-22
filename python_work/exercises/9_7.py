# Admin
from user import User


class Admin(User):
    """A class representing an admin user."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize the admin user."""
        super().__init__(first_name, last_name, username, email)
        self.privileges = Privileges()
