great_ppl_list: list[str] = ["Mark Hamill", "Luke Skywalker", "The Joker"]
for person in great_ppl_list:
    invitation_message = f"I would like to invite you, {person.title()}, to my dinner."
    print(invitation_message)
print(f"Unfortunately, {great_ppl_list[0].title()} can't make it to the dinner.")
substitute_person = "Harrison Ford"
great_ppl_list[0] = substitute_person
for person in great_ppl_list:
    invitation_message = f"I would like to invite you, {person.title()}, to my dinner."
    print(invitation_message)
