# People
from typing import TypedDict

class Person(TypedDict):
    first_name: str
    last_name: str
    age: int
    city: str

people: list[Person] = [
    {
        "first_name": "John",
        "last_name": "Doe",
        "age": 30,
        "city": "New York",
    },
    {
        "first_name": "Jane",
        "last_name": "Smith",
        "age": 25,
        "city": "Los Angeles",
    },
    {
        "first_name": "Alice",
        "last_name": "Johnson",
        "age": 28,
        "city": "Chicago",
    },
]

for person in people:
    print(f"\nFullname: {person['first_name'].title()} {person['last_name'].title()}")
    print(f"\tAge: {person['age']}")
    print(f"\tCity: {person['city'].title()}")
