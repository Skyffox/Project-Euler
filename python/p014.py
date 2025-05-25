# pylint: disable=line-too-long
"""
Problem 14: Longest Collatz Sequence

Problem description:
Which starting number, under one million, produces the longest chain?

Answer: 837799
"""

from functools import cache
from utils import profiler


@cache
def collatz_sequence_length(n: int) -> int:
    """
    Compute the length of the Collatz sequence for a given number n.

    The Collatz sequence is defined as follows:
    - If n is even, the next number is n / 2.
    - If n is odd, the next number is 3n + 1.
    
    The function recursively computes the length of the Collatz sequence starting with `n`, 
    until it reaches the number 1.

    Args:
        n (int): The starting number for the Collatz sequence.

    Returns:
        int: The length of the Collatz sequence starting from n.
    """
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_sequence_length(n // 2)
    else:
        return 1 + collatz_sequence_length(3 * n + 1)


@profiler
def compute() -> int:
    """
    Find the starting number under one million that produces the longest Collatz sequence.

    Returns:
        int: The starting number under one million that generates the longest Collatz sequence.
    """
    longest_chain = 0
    start_num = 0

    # Check each number below one million
    for n in range(2, 10**6):
        chain_length = collatz_sequence_length(n)

        # Update if we find a longer chain
        if chain_length > longest_chain:
            longest_chain = chain_length
            start_num = n

    return start_num


if __name__ == "__main__":
    print(f"Problem 14: {compute()}")
