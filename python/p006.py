# pylint: disable=line-too-long
"""
Problem 1: Find the difference between the sum of the squares of the first one hundred
           natural numbers and the square of the sum.
Answer: 25164150
Execution time: 0.0000s
"""

from utils import profiler


@profiler
def compute() -> int:
    """Difference between sum of squares and square of sum"""
    n = 100
    square_sum = sum(x for x in range(1, n + 1))**2
    sum_square = sum(x**2 for x in range(1, n + 1))

    return square_sum - sum_square


if __name__ == "__main__":
    print(f"Problem 6: {compute()}")
