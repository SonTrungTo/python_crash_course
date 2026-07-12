# Stages of life
age: int = 18

if age < 2:
    stage: str = "a baby"
elif age < 4:
    stage: str = "a toddler"
elif age < 13:
    stage: str = "a child"
elif age < 20:
    stage: str = "a teenager"
elif age < 65:
    stage: str = "an adult"
else:
    stage: str = "an elder"

print(f"You are {stage}.")
