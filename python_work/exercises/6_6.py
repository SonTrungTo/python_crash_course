# Polling
favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
pollers = ['jen', 'john', 'sam', 'sarah', 'grim']

for poller in pollers:
    if poller in favourite_languages.keys():
        print(f"Thank you for participating in the poll, {poller.title()}!")
    else:
        print(f"{poller.title()}, please take our poll.")
