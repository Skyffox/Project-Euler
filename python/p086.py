# pylint: disable=line-too-long
"""
Problem 86: Cuboid Route

Problem description:
This problem involves finding cuboids with integer dimensions, where the shortest path between two opposite corners of the cuboid is an integer. 
The shortest path is given by the 3D distance formula:

    distance = (a^2 + b^2 + c^2)^0.5

The goal is to determine the smallest perimeter (a + b + c) where the number of such cuboids exceeds 1000.

Answer: 1818
"""

import itertools
import functools
import math
from utils import profiler


def is_square(number: int) -> bool:
    """
    Checks if a given number is a perfect square.
    
    Args:
        number (int): The number to check.
    
    Returns:
        bool: True if the number is a perfect square, otherwise False.
    """
    floor = int(math.sqrt(number))
    return floor**2 == number


@functools.cache
def shortest_path_is_integer(a: int, b_plus_c: int) -> bool:
    """
    Checks if the shortest path from one corner to the opposite corner of a cuboid results in an integer value.
    The path is an integer if the sum of squares of the dimensions (a^2 + b^2 + c^2) forms a perfect square.
    
    Args:
        a (int): One dimension of the cuboid.
        b_plus_c (int): The sum of the other two dimensions, \( b + c \).
    
    Returns:
        bool: True if the shortest path is an integer, otherwise False.
    """
    return is_square(a**2 + b_plus_c**2)


def multiplicity(a: int, b_plus_c: int) -> int:
    """
    Calculates how many valid (b, c) pairs exist such that the perimeter condition is satisfied.
        
    Args:
        a (int): The first dimension of the cuboid.
        b_plus_c (int): The sum of the other two dimensions \( b + c \).
    
    Returns:
        int: The number of valid (b, c) pairs that satisfy the condition.
    """
    if b_plus_c <= a + 1:
        return b_plus_c // 2
    else:
        return (2 * a - b_plus_c + 2) // 2


@profiler
def compute() -> int:
    """
    Computes the smallest perimeter for which the number of cuboids with integer path 
    lengths from one corner to the opposite corner exceeds 1000.
    
    The function iterates over increasing values of a and computes for each value the 
    number of valid cuboids with integer path lengths, checking if the count exceeds 1000.

    Returns:
        int: The smallest perimeter for which the number of cuboids exceeds 1000.
    """
    ceiling = 1000000 # We are looking for the first perimeter that exceeds this count
    result = 0 # This will keep track of the total number of valid cuboids

    # Iterate through increasing values of a
    for a in itertools.count(1):
        # For each a, check values for b+c from 1 to 2*a
        for b_plus_c in range(1, 2 * a + 1):
            if shortest_path_is_integer(a, b_plus_c):
                # Increment the result by the number of valid (b, c) pairs
                result += multiplicity(a, b_plus_c)
                # If the result exceeds the ceiling, return the current value of a
                if result > ceiling:
                    return a


if __name__ == "__main__":
    print(f"Problem 86: {compute()}")
