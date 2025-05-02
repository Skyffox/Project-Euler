# pylint: disable=line-too-long
"""
Problem 78: Coin Partitions

Problem description:
We are tasked with finding the first number n such that the partition number p(n)
is divisible by 1,000,000. The partition function p(n) gives the number of ways
an integer n can be written as the sum of positive integers.

We use the recurrence relation derived from Euler's Pentagonal Number Theorem to compute
partition numbers efficiently.

Answer: 55374
"""

from typing import List
from utils import profiler


def partition_numbers(limit: int)  -> List[int]:
    """
    Calculate partition numbers p(n) for all n up to the given limit using Euler's Pentagonal Number Theorem.
    
    Args:
        limit (int): The upper limit up to which partition numbers are calculated.
    
    Returns:
        list: A list where p[n] is the partition number for n, modulo 1,000,000.
    """
    # Initialize the list to store partition numbers with base case p(0) = 1.
    p = [0] * (limit + 1)
    p[0] = 1 # Base case: there's exactly one way to partition 0 (the empty sum).

    for n in range(1, limit + 1):
        total = 0
        k = 1
        while True:
            # Generalized pentagonal numbers: k * (3k - 1) / 2 and k * (3k + 1) / 2
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2

            # Break if the pentagonal numbers exceed n
            if pentagonal1 > n:
                break

            # Calculate the contribution of the current pentagonal numbers
            sign1 = -1 if k % 2 == 0 else 1
            total += sign1 * p[n - pentagonal1]

            if pentagonal2 <= n:
                sign2 = -1 if k % 2 == 0 else 1
                total += sign2 * p[n - pentagonal2]

            k += 1

        # Store the partition number modulo 1,000,000
        p[n] = total % 1000000

    return p


@profiler
def compute() -> int:
    """
    Find the first number n for which the partition number p(n) is divisible by 1,000,000.
    
    Returns:
        int: The first number n where p(n) % 1,000,000 == 0.
    """
    limit = 100000
    partitions = partition_numbers(limit)

    # Search for the first n where p(n) % 1,000,000 == 0
    for n in range(1, limit + 1):
        if partitions[n] == 0: # p(n) is divisible by 1,000,000
            return n

    return None


if __name__ == "__main__":
    print(f"Problem 78: {compute()}")
