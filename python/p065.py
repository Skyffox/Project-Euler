# pylint: disable=line-too-long
"""
Problem 65: Convergents of e

Problem description:
This module calculates the sum of digits of the numerator of the 100th convergent of the continued fraction for e.
The continued fraction representation for e is given by:

    e = [2; 1, 2, 1, 1, 4, 1, 1, 6, 1, 1, 8, ...]

The 100th convergent is derived from a sequence of fractions that approximates e. 
The goal is to compute the sum of the digits of the numerator of the 100th convergent.

Answer: 272
"""

from utils import profiler


def digit_sum(num: int) -> int:
    """
    Calculates the sum of digits of a given number.
    
    Args:
        num (int): The number whose digits will be summed.
    
    Returns:
        int: The sum of the digits of the number.
    """
    total_sum = 0
    while num > 0:
        total_sum += num % 10 # Add the last digit to the sum
        num //= 10 # Remove the last digit
    return total_sum


@profiler
def compute() -> int:
    """
    Calculates the sum of the digits of the numerator of the N-th convergent of e's continued fraction.

    Returns:
        int: Returns the sum of digits of the numerator of the N-th convergent.
    """
    # Initial values for the continued fraction sequence for e
    n = 2
    prev_n = 1
    limit = 100 # Set the limit for the 100th convergent

    fract = 1
    for k in range(2, limit + 1):
        temp = prev_n
        if k % 3 == 0:
            fract = 2 * int(k / 3) # Every 3rd term is double the integer part
        else:
            fract = 1
        prev_n = n
        n = fract * prev_n + temp

    # Calculate the sum of digits of the numerator
    return digit_sum(n)


if __name__ == "__main__":
    print(f"Problem 65: {compute()}")
