# pylint: disable=line-too-long
"""
Problem 1: Multiples of 3 or 5

Problem description:
If we list all the natural numbers below 10 that are multiples of 3 or 5, 
we get 3, 5, 6, and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

Answer: 233168
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the sum of all multiples of 3 or 5 below 1000.

    This function iterates through all integers below 1000 and adds up those
    that are divisible by 3 or 5.

    Returns:
        int: The sum of all numbers below 1000 that are divisible by 3 or 5.
    """
    limit = 1000
    return sum(n for n in range(1, limit) if n % 3 == 0 or n % 5 == 0)


if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
