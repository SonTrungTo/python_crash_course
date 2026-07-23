# Admin
from user import User
from privileges import Privileges


class Admin(User):
    """A class representing an admin user."""

    def __init__(self, first_name, last_name, username, email):
        """Initialize the admin user."""
        super().__init__(
            first_name,
            last_name,
            username=username,
            email=email
        )
        self._privileges = Privileges()

    @property
    def privileges(self):
        """Get the privileges of the admin user."""
        return self._privileges


if __name__ == "__main__":
    print("Showing the admin user's privileges...")
    admin_user = Admin(
        "Son",
        "To",
        "Dishwasher92",
        "diswasher92@gmail.com"
    )
    admin_user.privileges.show_privileges()
