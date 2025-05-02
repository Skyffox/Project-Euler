# pylint: disable=no-name-in-module, line-too-long
"""
Problem 46: Goldbach's Other Conjecture

This module solves the problem proposed by Christian Goldbach, which states that every odd composite number 
can be written as the sum of a prime number and twice a square. The task is to find the smallest odd composite 
number that cannot be written in this way.

Answer: 5777
"""

import math
from utils import profiler, sieve_of_atkin


@profiler
def compute() -> int:
    """
    Finds the smallest odd composite number that cannot be written as the sum of a prime
    and twice a square.

    The conjecture states that every odd composite number can be expressed as the sum of 
    a prime number and twice a square (i.e., x = p + 2 * a^2). This function iterates 
    through odd composite numbers and checks if they satisfy this condition. The first 
    odd composite number that fails the conjecture is returned.

    Returns:
        int: The smallest odd composite number that cannot be written as the sum of a prime 
             and twice a square.
    """
    n = 6000 # Set an upper bound for prime number generation
    primes = sieve_of_atkin(n) # Generate primes up to the given limit

    # Loop through odd composite numbers greater than 1
    for x in range(9, n, 2):
        if x in primes:
            continue  # Skip prime numbers, as we are looking for composites

        found = False
        # Check if the number can be written as the sum of a prime and twice a square
        for p in primes:
            if p >= x:
                break # No need to check primes larger than x

            a_squared = (x - p) / 2 # Calculate the candidate square term
            a = math.sqrt(a_squared) # Check if the square root of the candidate is an integer
            if a.is_integer():
                found = True # This number satisfies the conjecture
                break

        if not found:
            return x # Return the first odd composite number that fails the conjecture


if __name__ == "__main__":
    print(f"Problem 46: {compute()}")
