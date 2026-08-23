import pytest
from exercises.employee import Employee

@pytest.fixture
def employee():
    """Fixture to create an Employee instance for testing."""
    return Employee("Son", "To", 50000)

def test_give_default_raise(employee):
    """Test giving a default raise of €5000."""
    employee.give_raise()
    assert employee.annual_salary == 55000

def test_give_custom_raise(employee):
    """Test giving a custom raise of €10000."""
    employee.give_raise(10000)
    assert employee.annual_salary == 60000
