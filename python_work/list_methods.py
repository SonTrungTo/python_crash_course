games: list[str] = ["requiem", "sc", "sq42", "kela", "ai"]

# append(), insert(), remove(), pop(), del, clear()
games.append("starfield")
print(games)
games.insert(0, "wings_commander")
print(games)
non_game = games.pop(-3)
print(f"{non_game.title()} is not a game. Popped!")
science_field = "ai"
print(f"Removing {science_field.title()} because it is not a game.")
games.remove(science_field)
del games[0]
print(f"After deleting the first game, we have: {games}")

games.clear()
print(f"After clearing the list, we have: {games}")
