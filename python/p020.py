# pylint: disable=line-too-long
"""
Problem 20: Factorial Digit Sum

Problem description:
The task is to find the sum of the digits in the number 100!. This involves computing the factorial of 100 
and then summing the digits of the resulting large number.

Answer: 648
"""

from math import factorial
from utils import profiler


@profiler
def compute() -> int:
    """
    Calculate the factorial of 100 and return the sum of its digits.

    Returns:
        int: The sum of the digits of 100!.
    """
    return sum(int(i) for i in str(factorial(100)))


if __name__ == "__main__":
    print(f"Problem 20: {compute()}")
