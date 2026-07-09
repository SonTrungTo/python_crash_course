# Buffet
buffet = ("soup", "kimchi", "salmon")
for food in buffet:
    print(f"{food.title()} is available at the buffet.")

#buffet[0] = "pasta"  # This will raise a TypeError because tuples are immutable
print(f"")
buffet = ("pasta", "kimchi", "salmon")  # Reassigning the entire tuple is allowed
for food in buffet:
    print(f"{food.title()} is available at the buffet. (revised)")
