from pathlib import Path

path = Path('pi_digits.txt')
contents = path.read_text().rstrip()
# Returns empty string when it reaches EOF 
# Remove any leading/trailing whitespace from the right
print(contents)
