# pylint: disable=line-too-long
"""
Problem 14: Which starting number, under one million, produces the longest chain
Answer: 
Execution time: 0.0000s
"""

from functools import cache
from utils import profiler


@cache
def collatz_sequence(n):
    """
    The Collatz sequence is defined for the set of positive integers:
    n → n / 2 (n is even)
    n → 3n + 1 (n is odd)
    """
    if n % 2 == 0:
        return n / 2
    else:
        return n * 3 + 1


@profiler
def compute():
    """Find the starting number that produces the largest Collatz sequence"""
    longest_chain = 0
    start_num = 0

    for n in range(2, 10**6):
        seq_start = n
        chain = 1
        while n != 1 or n > 1:
            n = collatz_sequence(n)
            chain += 1

        if chain > longest_chain:
            longest_chain = chain
            start_num = seq_start

    return start_num


if __name__ == "__main__":
    print(f"Problem 14: {compute()}")
