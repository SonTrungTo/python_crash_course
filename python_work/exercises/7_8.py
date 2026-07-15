# Deli
sandwich_orders: list[str] = [
    "tuna",
    "pepperoni",
    "turkey",
    "veggie",
    "pastrami",
    "salmon",
    "turkey",
    "cold_cuts"
]
finished_sandwiches: list[str] = []

while sandwich_orders:
    current_sandwich: str = sandwich_orders.pop(0)
    print(f"I made your {current_sandwich} sandwich.")
    finished_sandwiches.append(current_sandwich)

print("\nThe following sandwiches have been made:")
for sandwich in finished_sandwiches:
    print(f"- {sandwich}")