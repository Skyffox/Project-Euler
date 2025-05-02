# pylint: disable=line-too-long
"""
Problem 70: Totient Permutation

Problem description:
This module solves the problem of finding the value of n, 1 < n < 10^7, for which:
1. The Euler's Totient function φ(n) is a permutation of n.
2. The ratio n / φ(n) is minimized.

Euler's Totient function φ(n) counts the number of integers from 1 to n that are coprime with n.
The goal is to minimize the ratio n / φ(n).

Answer: 8319823
"""

from typing import List
from utils import profiler


def list_totients(n: int) -> List[int]:
    """
    Generates a list of Euler's Totient values for all integers from 1 to n.
    
    Args:
        n (int): The upper bound up to which totients are computed.
    
    Returns:
        List[int]: A list of totient values for numbers from 1 to n.
    """
    result: list[int] = list(range(n + 1))
    for i in range(2, len(result)):
        if result[i] == i: # i is prime
            for j in range(i, len(result), i):
                result[j] -= result[j] // i
    return result


@profiler
def compute() -> str:
    """
    Computes the value of n, 1 < n < 10^7, for which φ(n) is a permutation of n and the ratio n / φ(n) is minimized.
    
    This function generates the totients for numbers up to 10^7 and finds the number n where the condition holds.
    
    Returns:
        str: The value of n as a string for which φ(n) is a permutation of n and n / φ(n) is minimized.
    """
    totients = list_totients(10**7 - 1)
    minnumer = 1
    mindenom = 0

    for (i, tot) in enumerate(totients[2:], 2):
        # Check if n and φ(n) are permutations and if the ratio is minimized
        if i * mindenom < minnumer * tot and sorted(str(i)) == sorted(str(tot)):
            minnumer = i
            mindenom = tot
    return str(minnumer)


if __name__ == "__main__":
    print(f"Problem 70: {compute()}")
