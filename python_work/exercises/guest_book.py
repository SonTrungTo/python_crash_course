from pathlib import Path

path = Path(__file__).parent / 'text_files' / 'guest_book.txt'
path.parent.mkdir(parents=True, exist_ok=True)

all_names: list[str] = []
try:
    while True:
        name = input("What is your name? (enter 'q' to quit) ")
        if not name.strip():
            print("Please enter a valid name.")
            continue
        if name == 'q':
            break
        else:
            formatted_name = name.title()
            print(f"Hello, {formatted_name}!")
            all_names.append(formatted_name)
finally:
    path.write_text('\n'.join(all_names) + '\n')
