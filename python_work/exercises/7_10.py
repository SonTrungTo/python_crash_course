# Dream Vacation
import signal

dream_vacations: dict[str, str] = {}
poll_results: dict[str, int] = {}


def handle_sigterm(signum, frame):
    raise KeyboardInterrupt


signal.signal(signal.SIGTERM, handle_sigterm)

try:
    while True:
        user_name = input("What is your name? ")

        prompt = f"Hi {user_name}! Where would you like to go for your dream vacation?"
        prompt += " (Press Ctrl+C or send SIGTERM to exit and show results) "
        response = input(prompt)
        dream_vacations[user_name] = response
except KeyboardInterrupt:
    pass

print("\n\nDream Vacation Poll Results:")
for location in dream_vacations.values():
    if location in poll_results:
        poll_results[location] += 1
    else:
        poll_results[location] = 1

for location, count in poll_results.items():
    total_votes = sum(poll_results.values())
    percentage = (count / total_votes) * 100
    print(f"{location}: {percentage:.2f}% ({count})")
