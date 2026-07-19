# Messages
tms = [
    "Hello, how are you?",
    "I'm doing well, thank you!",
    "What about you?",
    "I'm good too!",
    ]

def show_messages(messages: list[str]) -> None:
    """Prints each message in the list."""
    for message in messages:
        print(message)

show_messages(tms)
