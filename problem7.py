# pylint: disable=line-too-long, no-name-in-module
"""
Problem 1: What is the 10001st prime number.
Answer: 104743
"""

from utils import sieve_of_atkin

if __name__ == "__main__":
    print(f"Problem 7: {sieve_of_atkin(150000)[10001]}")
