# Movie tickets

while True:
    age = input("How old are you? ")
    if age == 'quit' or age == 'exit':
        break
    if int(age) < 3:
        print("Your ticket is free.")
    elif int(age) <= 12:
        print("Your ticket is $10.")
    else:
        print("Your ticket is $15.")
