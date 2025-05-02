# pylint: disable=line-too-long
"""
Problem 2: Even Fibonacci numbers

Problem description:
By considering the terms in the Fibonacci sequence whose values do not
exceed four million, find the sum of the even-valued terms.

Answer: 4613732
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the sum of all even Fibonacci numbers that do not exceed the given limit.

    This function generates Fibonacci numbers until they exceed the limit,
    and then calculates the sum of those that are even.

    Returns:
        int: The sum of the even Fibonacci numbers below the given limit.
    """
    # Initialize the first two Fibonacci numbers
    first, second = 1, 2
    total_sum = 0
    limit = 4000000

    # Generate Fibonacci numbers and sum the even ones
    while second <= limit:
        if second % 2 == 0:
            total_sum += second
        first, second = second, first + second

    return total_sum


if __name__ == "__main__":
    print(f"Problem 2: {compute()}")
