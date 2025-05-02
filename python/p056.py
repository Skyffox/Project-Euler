# pylint: disable=line-too-long
"""
Problem 56: Powerful Digit Sum

Problem description:
We are tasked with finding the maximum digital sum of numbers of the form a^b, where a and b are natural numbers less than 100. 
The digital sum is the sum of the digits of the number. For example, 2^15 = 32768 and the digital sum is 3 + 2 + 7 + 6 + 8 = 26.

Answer: 972
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the maximum digital sum for numbers of the form a^b, where a and b are less than 100.
    
    The digital sum is the sum of the digits of a number. This function iterates over all possible values
    of a and b (both ranging from 1 to 99), calculates a^b, then computes the digital sum of the result.
    The maximum digital sum found is returned.
    
    Returns:
        int: The maximum digital sum.
    """
    largest_s = 0
    # Iterate over all a, b where a, b < 100
    for a in range(1, 101):
        for b in range(1, 101):
            # Calculate a^b
            n = a ** b
            # Calculate the sum of the digits
            s = sum(int(digit) for digit in str(n))
            # Track the maximum digital sum
            largest_s = max(largest_s, s)

    return largest_s


if __name__ == "__main__":
    print(f"Problem 56: {compute()}")
