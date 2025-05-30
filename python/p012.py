# pylint: disable=line-too-long
"""
Problem 12: Highly Divisible Triangular Number

Problem description:
The sequence of triangle numbers is generated by adding the natural numbers:
    T_n = 1 + 2 + 3 + ... + n

The problem asks to find the first triangle number that has more than 500 divisors.

The solution involves calculating triangle numbers sequentially, counting the divisors of each number, 
and checking if the number of divisors exceeds 500.

Answer: 76576500
"""

from math import sqrt
from utils import profiler


def count_divisors(n: int) -> int:
    """
    Count the number of divisors of a number n by iterating up to the square root of n.

    A divisor of n is a number i such that n % i == 0. For each i, n // i is also a divisor unless i == n // i.

    Parameters:
    n (int): The number for which divisors need to be counted.

    Returns:
    int: The number of divisors of n.
    """
    divisors = 0
    for i in range(1, int(sqrt(n)) + 1):
        if n % i == 0:
            divisors += 2 if i != n // i else 1
    return divisors


@profiler
def compute() -> int:
    """
    Find the first triangle number with more than 500 divisors.

    A triangle number is the sum of the natural numbers up to n:
        T_n = 1 + 2 + 3 + ... + n = n * (n + 1) // 2
    The task is to calculate the triangle numbers sequentially, count the divisors of each triangle number,
    and find the first one that has more than 500 divisors.

    Returns:
    int: The first triangle number with more than 500 divisors.
    """
    n = 1
    while True:
        # Calculate the nth triangle number using the formula T_n = n * (n + 1) // 2
        triangle_number = n * (n + 1) // 2

        # If the total divisors exceed 500, return the triangle number
        if count_divisors(triangle_number) > 500:
            return triangle_number

        n += 1


if __name__ == "__main__":
    print(f"Problem 12: {compute()}")
