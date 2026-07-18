# Large Shirts
def make_large_shirt(size="L", message="I love Python"):
    """Display a summary info about the shirt size and its message, modified"""
    info = f"The shirt, which is of size {size}, "
    info += f"has a printed message '{message}' on it."
    print(info)

make_large_shirt()
make_large_shirt(size="M")
make_large_shirt(size="XL", message="I don't like programming!")
