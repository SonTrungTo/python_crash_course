# T-Shirt
def make_shirt(size, message):
    """Display a short summary about the shirt size and message."""
    info = f"The shirt, which is of size {size}, "
    info += f"has a printed message '{message}' on it."
    print(info)

make_shirt("L", "I love Python")
make_shirt(size="L", message="I love Python")
make_shirt(size="M", message="Python is awesome!")
