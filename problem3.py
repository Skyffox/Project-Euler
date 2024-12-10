# pylint: disable=line-too-long
"""
Problem 1: What is the largest prime factor of the number 600851475143.
           A prime factor of a positive integer are prime numbers that divide that integer exactly.
Answer: 6857
Execution time: 0.0000s
"""

from utils import profiler

@profiler
def largest_prime_number(limit: int) -> int:
    """Find the largest prime number till a certain limit"""
    i = 2
    while i * i < limit:
        while limit % i == 0:
            limit //= i
        i += 1

    return limit


if __name__ == "__main__":
    print(f"Problem 3: {largest_prime_number(600851475143)}")
