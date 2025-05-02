# pylint: disable=no-name-in-module, line-too-long
"""
Problem 77: Prime Summations

Problem description:
We are tasked with finding the smallest number that can be expressed as a sum of primes in more than 5000 ways.
The solution uses dynamic programming to count the number of ways to express a number as a sum of primes.

Answer: 71
"""

from typing import List
from utils import profiler, sieve_of_atkin


def count_prime_sum_ways(limit: int, primes: List[int]) -> List[int]:
    """
    Count the number of ways each number up to limit can be expressed as a sum of primes.

    Args:
        limit (int): The upper limit to which sums are counted.
        primes (list): List of prime numbers used to form sums.

    Returns:
        list: The number of ways each number can be expressed as a sum of primes.
    """
    ways = [0] * (limit + 1)
    ways[0] = 1 # There's one way to sum to zero (using no primes)

    for prime in primes:
        for i in range(prime, limit + 1):
            ways[i] += ways[i - prime]

    return ways


@profiler
def compute() -> int:
    """
    Find the smallest number that can be written as a sum of primes in more than 5000 ways.

    Returns:
        int: The smallest number that can be written as a sum of primes in more than 5000 ways.
    """
    limit = 1000
    primes = sieve_of_atkin(limit) # Generate all primes up to limit
    ways = count_prime_sum_ways(limit, primes)

    for i in range(2, limit + 1):
        if ways[i] > 5000:
            return i

    return None


if __name__ == "__main__":
    print(f"Problem 77: {compute()}")
