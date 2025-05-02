# pylint: disable=line-too-long
"""
Problem 3: Largest prime factor

Problem description:
What is the largest prime factor of the number 600851475143?
A prime factor of a positive integer is a prime number that divides that integer exactly.

Answer: 6857
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Finds the largest prime factor of the number 600851475143.

    This function iteratively divides the given number by its smallest prime factor
    until the largest prime factor is found.

    Returns:
        int: The largest prime factor of 600851475143.
    """
    number = 600851475143
    i = 2

    # Loop through possible factors
    while i * i <= number:
        while number % i == 0:
            number //= i
        i += 1

    return number


if __name__ == "__main__":
    print(f"Problem 3: {compute()}")
