# User Profile
def build_profile(first: str, last: str, **user_info: str) -> dict[str, str]:
    """Build a dictionary containing everything we know about a user."""
    profile = {}
    user_info['first_name'] = first
    user_info['last_name'] = last
    for key in sorted(user_info.keys()):
        profile[key] = user_info[key]
    return profile


user_profile = build_profile(
    'son',
    'to',
    character='resilient',
    personality='radical',
    hobby='gaming'
    )
print(user_profile)
