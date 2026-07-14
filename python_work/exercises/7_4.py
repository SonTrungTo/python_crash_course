# Pizza Toppings
still_adding_toppings = True

while still_adding_toppings:
    topping = input("Enter a pizza topping: ")
    if topping == 'quit':
        still_adding_toppings = False
    else:
        print(f"Adding {topping} to your pizza.")
