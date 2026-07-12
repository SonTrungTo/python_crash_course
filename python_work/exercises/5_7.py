# Favourite fruit
favourite_fruits = ['banana', 'apple', 'orange', 'grape', 'mango']
while True:
    try:
        favourite_fruit = input("What is your favourite fruit?\n")
        if favourite_fruit.lower() in favourite_fruits:
            print(f"You really like {favourite_fruit.lower()}s!")
    except ValueError as e:
        print(e)