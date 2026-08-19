from decimal import Decimal, getcontext
from math import factorial
from random import random

getcontext().prec = 50  # digits of precision

def arctan(x):
    x = Decimal(x)
    x2 = x * x
    term = x
    total = x
    n = 1
    sign = -1
    while True:
        term *= x2
        delta = term / (2 * n + 1)
        if delta == 0:
            break
        total += sign * delta
        sign = -sign
        n += 1
    return total

# Machin: π = 16·arctan(1/5) − 4·arctan(1/239)
def compute_machin_pi():
    pi = 16 * arctan(Decimal(1) / 5) - 4 * arctan(Decimal(1) / 239)
    return pi

# Chudnovsky: π = 12 * Σ (−1)^k * (6k)! / ((3k)! * (k!)^3 * 640320^(3k + 3/2)) (used in mpmath library)
def compute_chudnovsky_pi():
    k = 0
    total = Decimal(0)
    while True:
        numerator = Decimal((-1) ** k) * factorial(6 * k)
        denominator = Decimal(factorial(3 * k)) * (Decimal(factorial(k)) ** 3) * (Decimal(640320) ** (3 * k + Decimal('1.5')))
        term = numerator / denominator
        if term == 0:
            break
        total += term
        k += 1
    pi = Decimal(12) * total
    return pi

# Monte Carlo simulation to estimate π
def monte_carlo_pi(num_samples):
    inside_circle = 0
    for _ in range(num_samples):
        x = random()
        y = random()
        if x * x + y * y <= 1:
            inside_circle += 1
    pi_estimate = Decimal(4) * Decimal(inside_circle) / Decimal(num_samples)
    return pi_estimate
