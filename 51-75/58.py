#! /usr/bin/python3

# Naam     : Julius
# UvAnetID : 11109602
# Studie   : BSc Informatica

# 58.py:


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


c = 1
last_num = 9
width = 3

primes = 0
total = 0

while True:
    # See what numbers are along the diagonals.
    # Fourth diagonal is never prime.
    if is_prime(c + width - 1):
        primes += 1

    if is_prime(c + 2 * (width - 1)):
        primes += 1

    if is_prime(c + 3 * (width - 1)):
        primes += 1

    total += 4

    if ((primes / total) * 100) < 10.0:
        break

    width += 2
    c = last_num
    last_num = width**2

# Minus 2 since counted starting width double.
print("Length of the spiral when ratio of primes is below 10%:", width - 2)
