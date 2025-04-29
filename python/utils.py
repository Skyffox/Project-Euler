# pylint: disable=line-too-long
"""
Useful functions to help with Euler problems
"""

from functools import wraps
import time
import math


def profiler(func):
    """Allows for a timing decorator on a function"""
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args,**kwargs)
        print(f'Time taken by function {func.__name__} is: {time.time() - start:0.4f} seconds')

        return result
    return wrapper


def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i * i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


def sieve_of_atkin(limit):
    """
    The sieve of Atkin is a modern algorithm for finding all prime numbers up to a specified integer. 
    Compared with the ancient sieve of Eratosthenes, which marks off multiples of primes, 
    the sieve of Atkin does some preliminary work and then marks off multiples of squares of primes.
    """
    primes = [2, 3]
    sieve = [False] * (limit + 1)
    for x in range(1, int(math.sqrt(limit)) + 1):
        for y in range(1, int(math.sqrt(limit)) + 1):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                sieve[n] = not sieve[n]

            n = 3 * x ** 2 + y ** 2
            if n <= limit and n % 12 == 7:
                sieve[n] = not sieve[n]

            n = 3 * x ** 2 - y ** 2
            if x > y and n <= limit and n % 12 == 11:
                sieve[n] = not sieve[n]

    for x in range(5, int(math.sqrt(limit))):
        if sieve[x]:
            for y in range(x ** 2, limit + 1, x ** 2):
                sieve[y] = False

    for p in range(5, limit):
        if sieve[p]:
            primes.append(p)

    return primes
