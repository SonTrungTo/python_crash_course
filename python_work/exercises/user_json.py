from pathlib import Path
from pydantic import BaseModel, ValidationError, EmailStr

class UserInfo(BaseModel):
    name: str
    age: int
    email: EmailStr

def read_stored_user_info(path: Path) -> UserInfo | None:
    """Read the stored user information from a JSON file."""
    if path.exists():
        try:
            # Parse and check value at the same time.
            return UserInfo.model_validate_json(path.read_text())
        except ValidationError as e:
            print(f"Stored data is invalid: {e}")
            # For symmetry of intent, return None, not just a syntax issue
            return None
    return None

def get_new_user_info(path: Path) -> UserInfo | None:
    """Prompt the user for their information and return it as a dictionary."""
    user_info = UserInfo(
        name = input("Enter your name: ").title(),  # capitalize first letter of each word
        age = input("Enter your age: "),            # str coerced to int
        email = input("Enter your email: "),        # raises ValidationError if malformed
    )
    path.write_text(user_info.model_dump_json(indent=2) + '\n')
    return user_info

def greet_user():
    """Greet the user based on stored or new information."""
    file_path = Path(__file__).parent / 'user_data' / 'user_info.json'
    user_info = read_stored_user_info(file_path)
    is_correct_user = input(f"Are you {user_info.name}? (y/n): ").strip().lower() if user_info else 'n'
    if is_correct_user == 'y':
        message = f"Welcome back, {user_info.name}!"
        message += f" "
        message += f"You are {user_info.age} years old and your email is {user_info.email}."
        print(message)
    elif is_correct_user == 'n':
        new_user_info = get_new_user_info(file_path)
        print(f"Thank you, {new_user_info.name}! Your information has been saved.")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    greet_user()
