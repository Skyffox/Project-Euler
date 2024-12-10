# pylint: disable=line-too-long
"""
Problem 1: Find the sum of all the multiples of 3 or 5 below 1000.
Answer: 233168
Execution time: 0.0000s
"""

from utils import profiler

@profiler
def sum_of_multiples(r: int) -> int:
    """Find multiples of 3 and 5"""
    return sum([n for n in range(1, r) if n % 3 == 0 or n % 5 == 0])


if __name__ == "__main__":
    print(f"Problem 1: {sum_of_multiples(1000)}")
