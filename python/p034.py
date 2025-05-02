# pylint: disable=line-too-long
"""
Problem 34: Digit Factorials

Problem description:
145 is a curious number because 1! + 4! + 5! = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.

Answer: 40730
"""

import math
from utils import profiler

# Precompute factorials of digits 0–9
DIGIT_FACTORIALS = [math.factorial(i) for i in range(10)]


@profiler
def compute() -> int:
    """
    Computes the sum of all numbers equal to the sum of the factorial of their digits.

    Returns:
        int: The total sum of all 'curious' numbers.
    """
    # Upper bound estimate: 7 * 9! = 2,540,160
    upper_limit = 7 * DIGIT_FACTORIALS[9]
    total = 0

    for num in range(10, upper_limit):
        digit_sum = sum(DIGIT_FACTORIALS[int(d)] for d in str(num))
        if num == digit_sum:
            total += num

    return total


if __name__ == "__main__":
    print(f"Problem 34: {compute()}")
