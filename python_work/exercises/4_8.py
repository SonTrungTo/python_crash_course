# Make a list of cubes from 1 to 10
LIST = [num**3 for num in range(1, 11)]
LIST_STRING = "\n".join(f"{num}^3={num**3}" for num in range(1, 11))
print(f"list of cubes from 1 to 10:\n{LIST_STRING}")
