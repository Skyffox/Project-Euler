# pylint: disable=line-too-long
"""
Problem 47: Distinct Prime Factors

Problem Description:
We are asked to find the first four consecutive integers to have four distinct prime factors each. 
The goal is to identify the first number in a sequence of four consecutive integers, 
where each of these numbers has exactly four distinct prime factors.

To solve this, we generate prime numbers and check the number of distinct prime factors for each integer. 
Once we find four consecutive numbers with exactly four distinct prime factors, 
we return the first number of this sequence.

Answer: 134043
"""

from typing import Set
from utils import profiler


def prime_factors(n: int) -> Set[int]:
    """
    Returns the distinct prime factors of a number n.
    
    Args:
        n (int): The number to factorize.
    
    Returns:
        set: A set containing distinct prime factors of n.
    """
    factors = set()
    d = 2
    # Check for each number from 2 upwards as a potential factor
    while d * d <= n:
        while (n % d) == 0:
            factors.add(d)
            n //= d
        d += 1
    if n > 1: # If n is prime and greater than 1, it must be a factor.
        factors.add(n)
    return factors


@profiler
def compute() -> int:
    """
    Finds the first number that begins a sequence of four consecutive integers, each with exactly 4 distinct prime factors.
    
    Returns:
        int: The first number of the four consecutive integers with four distinct prime factors.
    """
    # Start checking from 2
    consecutive = 0
    n = 2
    while True:
        # Check the number of distinct prime factors
        if len(prime_factors(n)) == 4:
            consecutive += 1
        else:
            consecutive = 0 # Reset if the number doesn't meet the condition

        if consecutive == 4:
            return n - 4 + 1 # Return the first number in the sequence

        n += 1


if __name__ == "__main__":
    print(f"Problem 47: {compute()}")
