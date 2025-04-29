# pylint: disable=line-too-long
"""
Problem 20: Find the sum of the digits in the number 100!
Answer: 648
Execution time: 0.0000s
"""

from math import prod
from utils import profiler


@profiler
def compute():
    """Calculate the factorial of 100 and calculate the sum of its digits"""
    return sum([int(i) for i in str(prod(list(range(1, 101))))])


if __name__ == "__main__":
    print(f"Problem 20: {compute()}")
