# pylint: disable=no-name-in-module, line-too-long
"""
Problem 49: Prime Permutations

Problem Description:
We are tasked with finding a 12-digit number formed by concatenating the terms of an arithmetic sequence where:
1. Each term is prime.
2. The terms are permutations of each other.

For example, the sequence 1487, 4817, and 8147 forms such an arithmetic sequence where:
- The difference between each pair of terms is constant.
- All terms are prime.
- All terms are permutations of the same digits.

The goal is to identify the sequence of three 4-digit prime numbers that satisfy these properties and concatenate them to form a 12-digit number.

Answer: 296962999629
"""

from utils import profiler, sieve_of_atkin


def are_permutations(*args: int) -> bool:
    """
    Check if all the given numbers are permutations of each other.
    
    Args:
        *args (int): Numbers to check for being permutations of each other.
    
    Returns:
        bool: True if all the numbers are permutations of each other, otherwise False.
    """
    str_args = [sorted(str(x)) for x in args]
    return all(x == str_args[0] for x in str_args)


@profiler
def compute() -> int:
    """
    Finds the 12-digit number formed by concatenating the three 4-digit primes in an arithmetic sequence,
    where each term is a permutation of the others.

    Returns:
        int: The 12-digit number formed by concatenating the three primes in the sequence.
    """
    # Make 4 digit primes and remove the example
    primes = [x for x in sieve_of_atkin(9999) if x > 1000 and x != 1487]
    prime_set = set(primes) # To make prime lookups faster

    for p in primes:
        for q in primes:
            if p >= q:
                continue
            diff = q - p
            r = q + diff # The third prime in the sequence

            # Ensure that r is a prime and that p, q, r are distinct
            if r in prime_set and p != q and q != r and r != p:
                # Check if p, q, r are permutations of each other
                if are_permutations(p, q, r):
                    return int(''.join(map(str, [p, q, r])))

    return None


if __name__ == "__main__":
    print(f"Problem 49: {compute()}")
