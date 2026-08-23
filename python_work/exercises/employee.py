class Employee:
    """A class to represent an employee."""

    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the employee with first name, last name, and annual salary."""
        self.annual_salary = annual_salary
        self.first_name = first_name
        self.last_name = last_name

    def give_raise(self, amount=5000):
        """Give the employee a raise by the specified amount."""
        self.annual_salary += amount
