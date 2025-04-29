# pylint: disable=line-too-long
"""
Problem 1: What is the smallest positive number that is divisible by all of the number from 1 to 20.
Answer: 232792560
Execution time: 0.0000s
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Method is to start with a product of all prime numbers, such that that number is already 
    divisible by all prime numbers, the eventual total must then be a multiple of that number
    """
    prime_numbers_product = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    total = prime_numbers_product
    while True:
        if all([total % num == 0 for num in range(2, 21)]):
            break
        total += prime_numbers_product

    return total


if __name__ == "__main__":
    print(f"Problem 5: {compute()}")
