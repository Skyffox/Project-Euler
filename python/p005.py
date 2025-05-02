# pylint: disable=line-too-long
"""
Problem 5: Smallest multiple

Problem description:
What is the smallest positive number that is divisible by all of the numbers from 1 to 20?

Answer: 232792560
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the smallest positive number that is divisible by all numbers from 1 to 20.

    The method starts with the product of all prime numbers less than or equal to 20, ensuring 
    that the number is divisible by all primes. Then it iterates through multiples of this product 
    until a number divisible by all numbers from 1 to 20 is found.

    Returns:
        int: The smallest positive number divisible by all numbers from 1 to 20.
    """
    # The product of all prime numbers from 1 to 20
    prime_numbers_product = 2 * 3 * 5 * 7 * 11 * 13 * 17 * 19
    total = prime_numbers_product

    # Iterate to find the smallest multiple divisible by all numbers from 1 to 20
    while True:
        if all(total % num == 0 for num in range(2, 21)):
            break
        total += prime_numbers_product

    return total


if __name__ == "__main__":
    print(f"Problem 5: {compute()}")
