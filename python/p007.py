# pylint: disable=no-name-in-module, line-too-long
"""
Problem 7: 10001st prime

Problem description:
What is the 10001st prime number?

Answer: 104743
"""

from utils import sieve_of_atkin, profiler


@profiler
def compute() -> int:
    """
    Computes the 10001st prime number using the Sieve of Atkin.

    The function generates a list of prime numbers using the Sieve of Atkin algorithm 
    and returns the 10001st prime number.

    Returns:
        int: The 10001st prime number.
    """
    # Generate prime numbers up to a specified limit
    primes = sieve_of_atkin(150000)

    # Return the 10001st prime number (index 10000)
    return primes[10000]


if __name__ == "__main__":
    print(f"Problem 7: {compute()}")
