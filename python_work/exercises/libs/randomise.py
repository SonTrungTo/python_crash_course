from random import random

def geometric_rand_unbounded(p: float = 0.5) -> int:
    """
    Returns positive integer. p is probability of returning count.
    P(count) = (1-p)^(n) * p for n = 0, 1, 2, 3, ...
    """
    if not (0 < p < 1):
        raise ValueError("p must be in the range (0, 1)")
    
    count = 0
    while True:
        if random() < p:
            return count
        count += 1
    # while random() > p:
    #     count += 1
    # return count  

def rand_letter() -> str:
    """
    Returns a random letter.
    """
    letters = "abcdefghijklmnopqrstuvwxyz"
    return letters[round(random() * (len(letters) - 1))].upper()
