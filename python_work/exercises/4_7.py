# Make a list of multiples of 3 from 3 to 30
LIST = list(range(3, 31, 3))
LIST_STRING = ", ".join(str(num) for num in LIST)
print(f"list of multiples of 3 from 3 to 30: ({LIST_STRING})")
