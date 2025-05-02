# pylint: disable=line-too-long
"""
Problem 68: Magic 5-Gon Ring

Problem description:
This module solves the problem of finding the maximum 16-digit string that can be formed from 
a "magic" 5-gon ring using the numbers 1 to 10, where the sum of the numbers on each side of the 
5-gon is equal, and no number is repeated more than once.

Approach:
1. The numbers 1 to 10 are arranged in a circular, 5-gon configuration.
2. A "magic" 5-gon ring satisfies the condition that the sum of the numbers on each side is equal.
3. The goal is to find the maximum 16-digit string formed by the magic 5-gon where the string is formed by 
   concatenating the numbers on the sides in a particular order.

Answer: 6531031914842725
"""

import itertools
from typing import Tuple
from utils import profiler


def tuples_to_num(t: Tuple[int, int, int, int, int, int, int, int, int, int]) -> str:
    """
    Converts a tuple of integers into a concatenated string of numbers.
    
    Args:
        t (tuple): The tuple of integers.
    
    Returns:
        str: The concatenated string of integers.
    """
    return ''.join(''.join(str(i) for i in t))


def check(p: Tuple[int, int, int, int, int, int, int, int, int, int]) -> bool:
    """
    Checks if the given permutation satisfies the magic 5-gon ring conditions.
    
    Args:
        p (tuple): The permutation to check.
    
    Returns:
        bool: True if the permutation satisfies the magic 5-gon ring conditions, otherwise False.
    """
    # Check that no 10 is used in the circle as it would be counted twice
    if p[1] == 10 or p[2] == 10 or p[4] == 10 or p[6] == 10 or p[8] == 10:
        return False

    # Check that the first position is smaller than the other positions as per the problem requirements
    if p[0] > p[3] or p[0] > p[5] or p[0] > p[7] or p[0] > p[9]:
        return False

    # Check that all sides of the 5-gon have the same sum
    if p[0] + p[1] + p[2] != p[3] + p[2] + p[4]:
        return False
    if p[0] + p[1] + p[2] != p[5] + p[4] + p[6]:
        return False
    if p[0] + p[1] + p[2] != p[7] + p[6] + p[8]:
        return False
    if p[0] + p[1] + p[2] != p[9] + p[8] + p[1]:
        return False

    return True


@profiler
def compute() -> str:
    """
    Finds the maximum 16-digit string formed by the magic 5-gon ring configuration.
    
    Returns:
        str: The maximum 16-digit string.
    """
    # List of numbers to use in the 5-gon ring
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # Generate all possible permutations of the numbers
    permutations = list(itertools.permutations(nums, 10))
    reversed_permu = list(reversed(permutations))

    # Initialize solution variable
    solution = None

    # Iterate over the reversed permutations to find the valid "magic" 5-gon
    for p in reversed_permu:
        if check(p):
            # Form the 16-digit string from the valid magic 5-gon
            solution = [p[0], p[1], p[2], p[3], p[2], p[4], p[5], p[4],
                        p[6], p[7], p[6], p[8], p[9], p[8], p[1]]
            break # Break as soon as the first solution is found

    # Return the maximum 16-digit string
    return tuples_to_num(solution)


if __name__ == "__main__":
    print(f"Problem 68: {compute()}")
