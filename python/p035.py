# pylint: disable=no-name-in-module, line-too-long
"""
Problem 35: Circular Primes

Problem Description:
The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?

Answer: 55
"""

from typing import Set
from utils import profiler, sieve_of_atkin


def is_circular_prime(prime: int, primes_set: Set[int]) -> bool:
    """
    Checks whether a given prime number is a circular prime.
    
    A circular prime is a prime number that remains prime under any rotation of its digits.
    For example, 197 is a circular prime because all its rotations (197, 971, and 719) are also prime.

    Args:
        prime (int): The prime number to check.
        primes_set (set): A set containing all prime numbers up to the limit for fast lookups.

    Returns:
        bool: True if the given prime is a circular prime, False otherwise.
    """
    s = str(prime)
    for i in range(len(s)):
        rotated = int(s[i:] + s[:i]) # Rotate the digits
        if rotated not in primes_set:
            return False
    return True


@profiler
def compute() -> int:
    """
    Computes the number of circular primes below one million.

    Returns:
        int: The total number of circular primes below one million.
    """
    limit = 1000000
    primes = sieve_of_atkin(limit)
    primes_set = set(primes) # Use a set for fast lookup

    circular_primes = 0
    for prime in primes:
        if is_circular_prime(prime, primes_set):
            circular_primes += 1

    return circular_primes


if __name__ == "__main__":
    print(f"Problem 35: {compute()}")
