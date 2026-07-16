# No Pastrami
sandwich_orders: list[str] = [
    "tuna",
    "pastrami",
    "pepperoni",
    "turkey",
    "veggie",
    "pastrami",
    "salmon",
    "turkey",
    "pastrami",
    "cold_cuts"
]
finished_sandwiches: list[str] = []

print("The deli has run out of pastrami.")

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    current_sandwich: str = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")
