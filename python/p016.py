# pylint: disable=line-too-long
"""
Problem 16: What is the sum of the digits of the number 2^1000?
Answer: 
Execution time: 0.0000s
"""

from utils import profiler


@profiler
def compute():
    """Calculate big number cast to string and then a list and do a summation over all digits"""
    return sum([int(i) for i in str(2**1000)])


if __name__ == "__main__":
    print(f"Problem 16: {compute()}")
