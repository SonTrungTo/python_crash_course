# Sending Messages
tms = [
    "Hello, how are you?",
    "I'm doing well, thank you!",
    "What about you?",
    "I'm good too!",
    ]
sent_messages = []

def send_messages(messages: list[str], output_messages: list[str]) -> None:
    """Prints each message in the list."""
    while messages:
        current_message = messages.pop(0)
        print(f"Sending '{current_message}'")
        output_messages.append(current_message)

send_messages(tms, sent_messages)
print(f"\nOriginal list of messages: {tms}")
print(f"Sent messages: {sent_messages}")
