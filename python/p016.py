# pylint: disable=line-too-long
"""
Problem 16: Power Digit Sum

Problem description:
What is the sum of the digits of the number 2^1000?

Answer: 1366
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Calculate the sum of the digits of the number 2 raised to the power of 1000.

    This function computes 2^1000, converts it into a string, and then calculates 
    the sum of its digits. The result is returned as the sum of all individual digits 
    of the number.

    Returns:
        int: The sum of the digits of the number 2^1000.
    """
    return sum(int(digit) for digit in str(2**1000))


if __name__ == "__main__":
    print(f"Problem 16: {compute()}")
