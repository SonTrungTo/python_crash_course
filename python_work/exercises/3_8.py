# Seeing the world
world_interested_places = ['tokyo', 'berkeley', 'ho_chi_minh', 'palo_alto', 'massachusetts']

old_order = world_interested_places
new_order = sorted(world_interested_places)
reversed_new_order = sorted(world_interested_places, reverse=True)

print(f"Original order: {old_order}")
print(f"Sorted order: {new_order}")
print(f"Reversed sorted order: {reversed_new_order}")

print(f"Now, original order is directly modified...")

old_order.reverse()

print(f"Reversed original order: {old_order}")
print(f"Original list is now modified: {world_interested_places}")

old_order.reverse()
print(f"Original order is reversed again: {old_order}")
print(f"Original list is now re-reversed (restored): {world_interested_places}")

print(f"Original order is directly sorted...")

old_order.sort()
print(f"Sorted original order: {old_order}")
print(f"Original list is now sorted: {world_interested_places}")

old_order.sort(reverse=True)
print(f"Reversed sorted original order: {old_order}")
print(f"Original list is now reversed sorted: {world_interested_places}")