# pylint: disable=line-too-long
"""
Problem 23: Non-Abundant Sums

Problem description:
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 is 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n, and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two
abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the
sum of two abundant numbers.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

Answer: 4179871
"""

from math import isqrt
from utils import profiler


def is_abundant(n: int) -> bool:
    """
    Determines if a number n is abundant.

    Args:
        n (int): The number to check for abundance.

    Returns:
        bool: True if n is abundant, False otherwise.
    """
    total = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            total += i
            if i != n // i:
                total += n // i

    return total > n


@profiler
def compute() -> int:
    """
    Computes the sum of all positive integers that cannot be written as the sum of two abundant numbers.

    Returns:
        int: The sum of all positive integers that cannot be expressed as the sum of two abundant numbers.
    """
    limit = 28123

    # Generate list of abundant numbers
    abundants = [i for i in range(12, limit + 1) if is_abundant(i)]

    # Create a boolean array to mark numbers that can be written as the sum of two abundant numbers
    can_be_written = [False] * (limit + 1)

    # Mark sums of two abundant numbers
    for i, a in enumerate(abundants):
        for _, b in enumerate(abundants[i:], start=i):  # Start j from i to avoid redundant pairs
            s = a + b
            if s <= limit:
                can_be_written[s] = True
            else:
                break

    # Sum numbers that cannot be written as the sum of two abundant numbers
    return sum(i for i, x in enumerate(can_be_written) if not x)


if __name__ == "__main__":
    print(f"Problem 23: {compute()}")
