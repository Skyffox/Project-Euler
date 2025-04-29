# pylint: disable=line-too-long, no-name-in-module
"""
Problem 1: What is the 10001st prime number.
Answer: 104743
"""

from utils import sieve_of_atkin, profiler


@profiler
def compute():
    """Generate a list of prime numbers then take the 10001 number from that list"""
    return sieve_of_atkin(150000)[10000]


if __name__ == "__main__":
    print(f"Problem 7: {compute()}")
