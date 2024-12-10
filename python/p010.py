# pylint: disable=line-too-long, no-name-in-module
"""
Problem 1: Find the sum of all the primes below two million.
Answer: 142913828922
"""

from utils import sieve_of_atkin

if __name__ == "__main__":
    print(f"Problem 10: {sum(sieve_of_atkin(2000000))}")
