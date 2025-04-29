# pylint: disable=line-too-long, no-name-in-module
"""
Problem 1: Find the sum of all the primes below two million.
Answer: 142913828922
"""

from utils import sieve_of_atkin, profiler


@profiler
def compute():
    """Generate a list of prime number to a maximum of 2m"""
    return sum(sieve_of_atkin(2000000))


if __name__ == "__main__":
    print(f"Problem 10: {compute()}")
