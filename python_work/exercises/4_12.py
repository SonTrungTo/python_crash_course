### 4.12: More Loops
foods = ["ramen", "instant_noodles", "bbh"]

print(f"My favorite foods are: {", ".join([food for food in foods])}")
print(f"")
all_foods_str = ""
for food in foods:
    all_foods_str += f"{food}, "
print(f"My favorite foods are: {all_foods_str[:-2]}")
print(f"")
