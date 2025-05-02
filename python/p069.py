# pylint: disable=no-name-in-module, line-too-long
"""
Problem 69: Totient Maximum

Problem description:
This module solves the problem of finding the value of n ≤ 1,000,000 for which the ratio 
n/φ(n) is maximized. Where φ(n) is Euler's Totient function, which counts the number of integers 
less than n that are coprime with n.

The maximum value of n/φ(n) is made up from the product of prime numbers, as they have the simplest 
structure for calculating φ(n).

Answer: 510510
"""

from utils import profiler, sieve_of_atkin


@profiler
def compute() -> int:
    """
    Computes the value of n ≤ 1,000,000 for which n/φ(n) is maximized.

    Returns:
        int: The value of n for which n/φ(n) is maximum.
    """
    limit = 1000000
    sieve = sieve_of_atkin(limit)
    total = 1

    # Iterate through primes and multiply them together until total exceeds UPPER_BOUND
    for prime in sieve:
        total *= prime
        if total > limit:
            return total // prime  # Return the value of n for which n/φ(n) is maximized

    return -1


if __name__ == "__main__":
    print(f"Problem 69: {compute()}")
