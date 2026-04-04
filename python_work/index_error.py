motorcycles = ["Honda", "Yamaha", "Suzuki"]
for i, motorcycle in enumerate(motorcycles):
    motorcycles[i] = motorcycle.lower()
print(motorcycles)
print(motorcycles[3])  # This will raise an IndexError because there is no index 3 in the list.
