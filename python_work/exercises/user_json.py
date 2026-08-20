from pathlib import Path
import json

def read_stored_user_info():
    """Read the stored user information from a JSON file."""
    file_path = Path('user_info.json')
    if file_path.exists():
        with file_path.open('r') as file:
            user_info = json.load(file)
            return user_info
    return None
