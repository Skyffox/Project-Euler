# pylint: disable=line-too-long
"""
Problem 24: Lexicographic Permutations

Problem description:
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation
of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically,
we call it lexicographic order.

The lexicographic permutations of 0, 1 and 2 are:
    012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits
0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Answer: 2783915460
"""

import itertools
from utils import profiler


@profiler
def compute() -> str:
    """
    Computes the millionth lexicographic permutation of the digits 0 through 9.

    This function generates all possible permutations of the digits 0 through 9 in lexicographic order 
    using the `itertools.permutations` function. It iterates through the permutations and returns the 
    1,000,000th permutation as a string.

    Returns:
        str: The millionth lexicographic permutation of the digits 0 through 9.
    """
    permutations = itertools.permutations('0123456789')
    for idx, p in enumerate(permutations, 1):
        if idx == 1_000_000:
            return ''.join(p)


if __name__ == "__main__":
    print(f"Problem 24: {compute()}")
