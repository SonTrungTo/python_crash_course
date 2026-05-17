# Make a list of odd numbers from 1 to 20
LIST = list(range(1, 21, 2))
LIST_STRING = ", ".join(str(num) for num in LIST)
print(f"list of odd numbers from 1 to 20: ({LIST_STRING})")
