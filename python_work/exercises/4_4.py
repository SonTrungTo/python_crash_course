import time

DELAY = 0.5 # Delay in seconds
LIMIT = 10 ** 6 # 1 million
HOW_LONG = (DELAY * LIMIT) / (60 * 60 * 24) # How long to finish in days

list_required = [value for value in range(1, LIMIT + 1)]

print(f"To print numbers from 1 to {LIMIT} with a delay of {DELAY} seconds, it will take approximately {HOW_LONG:.2f} days.")
for value in list_required:
    print(value)
    time.sleep(DELAY) # Sleep for 0.1 seconds to slow down the output
