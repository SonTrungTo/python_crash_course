### 4.10 Slices
rts_games = ["starcraft", "warcraft_3", "company_of_heroes"]
mmo_space_games = ["star_citizen", "elite_dangerous", "eve_online"]
horror_games = ["resident_evil", "silent_hill", "dead_space"]

games = [*rts_games, *mmo_space_games, *horror_games]

DEFAULT_NUMBER_OF_GAMES = 3
print(f"games: {games}")

print(f"first {DEFAULT_NUMBER_OF_GAMES} games: {games[:DEFAULT_NUMBER_OF_GAMES]}")
print(f"middle {DEFAULT_NUMBER_OF_GAMES} games: {games[DEFAULT_NUMBER_OF_GAMES:(len(games) - DEFAULT_NUMBER_OF_GAMES)]}")
print(f"last {DEFAULT_NUMBER_OF_GAMES} games: {games[-DEFAULT_NUMBER_OF_GAMES:]}")
