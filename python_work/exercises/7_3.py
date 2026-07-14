# Multiples of 10
number_input = input("Enter a number: ")
if int(number_input) % 10 == 0:
    print(f"{number_input} is a multiple of 10.")
else:
    print(f"{number_input} is NOT a multiple of 10.")
