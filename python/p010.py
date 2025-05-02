# pylint: disable=no-name-in-module, line-too-long
"""
Problem 10: Summation of Primes

Problem description:
Find the sum of all the primes below two million.

Answer: 142913828922
"""

from utils import sieve_of_atkin, profiler


@profiler
def compute() -> int:
    """
    Sum all primes below two million using an efficient sieve.
    
    Returns:
        int: The sum of all prime numbers below two million.
    """
    limit = 2000000
    primes = sieve_of_atkin(limit)
    return sum(primes)


if __name__ == "__main__":
    print(f"Problem 10: {compute()}")
