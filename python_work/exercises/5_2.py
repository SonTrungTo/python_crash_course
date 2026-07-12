# More conditional tests§
print(f"Test for equality with strings: 'hello' == 'hello': I predict True.")
print('hello' == "hello")
print("")

print(f"Test for inequality with strings: 'hellos' < 'world': I predict True.")
print('hellos' < 'world')
print(f"This is because 'h' comes before 'w' in the alphabet: {ord('h')}, {ord('w')}")
print("")

print(f"Test using the 'lower' method: 'HeLlOs'.lower() == 'hellos': I predict True.")
print('HeLlOs'.lower() == 'hellos')
print("")

print(f"Test using numerical inequality: 2 >= 1, 2 > 1, 1 < 2, 1 <= 2: I predict True.")
print(2 >= 1, 2 > 1, 1 < 2, 1 <= 2)
print("")

print(f"Test using 'and'/'or' operators: (2 > 1 and 1 < 2) or (2 < 1): I predict True.")
print((2 > 1 and 1 < 2) or (2 < 1))
print("")

print(f"Test whether an item is in a list: 1 in [1, 2, 3]: I predict True.")
print(1 in [1, 2, 3])
print("")

print(f"Test whether an item is NOT in a list: 4 not in [1, 2, 3]: I predict True.")
print(4 not in [1, 2, 3])
print("")
