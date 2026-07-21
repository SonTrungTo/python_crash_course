# Login attempts
from user import User


class UserWithLoginAttempts(User):
    """A user class tracks login attempts."""

    def __init__(self, first_name, last_name, **info):
        """Initialise username and login attempts attributes."""
        super().__init__(first_name, last_name, **info)
        self._login_attempts = 0

    @property
    def login_attempts(self):
        """Get the number of login attempts."""
        return self._login_attempts

    def increment_login_attempts(self):
        """Increment the number of login attempts."""
        self._login_attempts += 1

    def reset_login_attempts(self):
        """Reset the number of login attempts."""
        self._login_attempts = 0

if __name__ == "__main__":
    print("Creating an instance of the UserWithLoginAttempts class...")
    user = UserWithLoginAttempts("John", "Doe", age=30, location="New York")
    user.describe_user()
    user.greet_user()

    # Increment login attempts
    print(f"Initial login attempts: {user.login_attempts}")
    user.increment_login_attempts()
    user.increment_login_attempts()
    print(f"Login attempts after incrementing: {user.login_attempts}")

    # Reset login attempts
    user.reset_login_attempts()
    print(f"Login attempts after reset: {user.login_attempts}")
