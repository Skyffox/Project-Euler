# pylint: disable=line-too-long
"""
Problem 6: Sum square difference

Problem description:
Find the difference between the sum of the squares of the first one hundred natural numbers 
and the square of the sum.

Answer: 25164150
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the difference between the sum of the squares and the square of the sum
    of the first 100 natural numbers.

    Returns:
        int: The difference between the sum of the squares and the square of the sum.
    """
    n = 100

    # Calculate the sum of the squares of the first n natural numbers
    sum_square = sum(x**2 for x in range(1, n + 1))

    # Calculate the square of the sum of the first n natural numbers
    square_sum = sum(x for x in range(1, n + 1))**2

    # Return the difference
    return square_sum - sum_square


if __name__ == "__main__":
    print(f"Problem 6: {compute()}")
