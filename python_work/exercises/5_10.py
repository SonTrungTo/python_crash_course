# Checking Usernames
current_users: list[str] = ['admin', 'user1', 'user2', 'user3', 'user3', 'user4']
new_users: list[str] = ['user5', 'User1', 'user6', 'AdMiN', 'user8']

for new_user in new_users:
    # () doesn't create a tuple, it creates a generator expression.
    # Also, using set(), not {{}} double curly braces, otherwise string interpolation happens and code is not evaluated.
    if new_user.lower() in set(user.lower() for user in current_users):
        print(f"Sorry {new_user}, that username is already taken.")
    else:
        print(f"Username {new_user} is available.")
