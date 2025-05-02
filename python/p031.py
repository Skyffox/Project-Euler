# pylint: disable=line-too-long
"""
Problem 31: Coin Sums

Problem description:
In England, the currency is made up of pounds (£) and pence (p). There are eight coins in general circulation:
    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).

It is possible to make £2 in the following way:
    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p

How many different ways can £2 be made using any number of coins?

Answer: 73682
"""

from typing import List
from utils import profiler


def count_ways_to_make_change(total: int, coins: List[int]) -> int:
    """
    Counts the number of ways to make a given total using a list of available coin denominations.
    
    This function uses a dynamic programming approach to count the ways to make change for a given total.
    It iterates through each coin denomination and updates the possible ways to form the total.
    
    Args:
        total (int): The total amount to be made (in pence).
        coins (list of int): The list of coin denominations available.

    Returns:
        int: The number of ways to make the total using the given coin denominations.
    """
    # Initialize a list to store the number of ways to make each value from 0 to total
    ways = [0] * (total + 1)
    ways[0] = 1 # There is 1 way to make 0 (using no coins)

    for coin in coins:
        # Update the ways to make each value from coin to total
        for i in range(coin, total + 1):
            ways[i] += ways[i - coin]

    return ways[total]


@profiler
def compute() -> int:
    """
    Computes the number of different ways to make £2 using any number of coins.

    Returns:
        int: The number of ways to make £2 using the available coins.
    """
    total = 200  # Total value of £2 in pence
    coins = [1, 2, 5, 10, 20, 50, 100, 200]  # Available coin denominations in pence
    return count_ways_to_make_change(total, coins)


if __name__ == "__main__":
    print(f"Problem 31: {compute()}")
