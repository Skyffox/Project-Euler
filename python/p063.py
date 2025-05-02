# pylint: disable=line-too-long
"""
Problem 63: Powerful Digit Counts

Problem description:
This module solves the problem of finding how many n-digit positive integers exist which are also an nth power.
The goal is to count how many numbers exist that satisfy the condition of being an nth power and having exactly `n` digits.

Answer: 49
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes how many n-digit positive integers exist which are also an nth power.

    Returns:
        int: The total count of n-digit numbers which are also an nth power.
    """
    n_digit = 0
    n = 1000

    # Iterate over all base (y) and exponent (x) combinations
    for x in range(1, n):
        for y in range(1, n):
            num = y ** x
            num_digits = len(str(num))

            # Break early if the number of digits exceeds the exponent
            if num_digits > x:
                break

            # If the number of digits equals the exponent, count it
            if num_digits == x:
                n_digit += 1

    return n_digit


if __name__ == "__main__":
    print(f"Problem 63: {compute()}")
