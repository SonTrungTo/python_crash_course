great_ppl_list: list[str] = ["Mark Hamill", "Luke Skywalker", "The Joker", "The King"]
for person in great_ppl_list:
    invitation_message = f"I would like to invite you, {person.title()}, to my dinner."
    print(invitation_message)

print(f"Invited {len(great_ppl_list)} people to the dinner.\n\n")

print(f"Unfortunately, {great_ppl_list[0].title()} can't make it to the dinner.")

substitute_person = "Harrison Ford"
great_ppl_list[0] = substitute_person
for person in great_ppl_list:
    invitation_message = f"I would like to invite you, {person.title()}, to my dinner."
    print(invitation_message)

print(f"Invited {len(great_ppl_list)} people to the dinner.\n\n")

print("Luckily, I have found a bigger table, so I can invite more people to the dinner!")
begin_pos = 0
print(f"Begin position: {begin_pos}")
great_ppl_list.insert(begin_pos, "Darth Vader")
middle_pos = len(great_ppl_list) // 2 # floor division, rounds DOWN to the nearest whole number, opposite for negative numbers
middle_pos_2 = -(-len(great_ppl_list) // 2) # ceil division, rounds UP to the nearest whole number, opposite for negative numbers
print(f"Middle position: {middle_pos_2}")
great_ppl_list.insert(middle_pos_2, "Princess Leia")
end_pos = len(great_ppl_list)
print(f"End position: {end_pos}")
great_ppl_list.insert(end_pos, "Emperor Palpatine")
for person in great_ppl_list:
    invitation_message = f"I would like to invite you, {person.title()}, to my dinner."
    print(invitation_message)

print(f"Invited {len(great_ppl_list)} people to the dinner.\n\n")

print("Unfortunately, I can only invite two people to the dinner.")
while len(great_ppl_list) > 2:
    removed_person = great_ppl_list.pop()
    print(f"Sorry, {removed_person.title()}, I can't invite you to the dinner.")
for person in great_ppl_list:
    invitation_message = f"You are still invited to the dinner, {person.title()}!"
    print(invitation_message)

print(f"Invited {len(great_ppl_list)} people to the dinner.\n\n")

while len(great_ppl_list) > 0:
    print(f"Removing {great_ppl_list[0].title()} from the list.")
    del great_ppl_list[0]
print(f"After deleting the remaining people, we have: {great_ppl_list}")
print(f"Invited {len(great_ppl_list)} people to the dinner.")
