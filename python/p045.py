# pylint: disable=line-too-long
"""
Problem 45: Triangle, Pentagonal, and Hexagonal

Problem Description:
The task is to find the next number that is simultaneously a triangle, pentagonal, 
and hexagonal number. The sequence starts at T285 = P165 = H143 = 40755.

A triangle number is given by Tn = n * (n + 1) / 2.
A pentagonal number is given by Pn = n * (3 * n - 1) / 2.
A hexagonal number is given by Hn = n * (2 * n - 1).

It can be verified that T285 = P165 = H143 = 40755.
The goal is to identify the next number in the sequence that satisfies all three formulas.

Answer: 1533776805
"""

from utils import profiler


def triangle(n: int) -> int:
    """
    Returns the nth triangle number.
    A triangle number is calculated by the formula Tn = n * (n + 1) / 2.

    Args:
        n (int): The index of the triangle number to return.

    Returns:
        int: The nth triangle number.
    """
    return n * (n + 1) // 2


def pentagonal(n: int) -> int:
    """
    Returns the nth pentagonal number.
    A pentagonal number is calculated by the formula Pn = n * (3 * n - 1) / 2.

    Args:
        n (int): The index of the pentagonal number to return.

    Returns:
        int: The nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


def hexagonal(n: int) -> int:
    """
    Returns the nth hexagonal number.
    A hexagonal number is calculated by the formula Hn = n * (2 * n - 1).

    Args:
        n (int): The index of the hexagonal number to return.

    Returns:
        int: The nth hexagonal number.
    """
    return n * (2 * n - 1)


@profiler
def compute():
    """
    Finds the next number that is both triangle, pentagonal, and hexagonal.

    Starting from known values (T285 = P165 = H143 = 40755), this function
    incrementally checks the triangle, pentagonal, and hexagonal sequences 
    to find the next common number that satisfies all three formulas.

    Returns:
        int: The next number that is simultaneously a triangle, pentagonal, 
             and hexagonal number.
    """
    # Start searching from n = 286 since we know T285 = P165 = H143 = 40755
    n = 286
    p = 166
    h = 144

    while True:
        # Generate the next triangle, pentagonal, and hexagonal numbers
        triangle_num = triangle(n)
        pentagonal_num = pentagonal(p)
        hexagonal_num = hexagonal(h)

        # If the triangle number is less than both pentagonal or hexagonal, increment n
        if triangle_num < pentagonal_num or triangle_num < hexagonal_num:
            n += 1
        # If the pentagonal number is less than the triangle or hexagonal, increment p
        elif pentagonal_num < triangle_num or pentagonal_num < hexagonal_num:
            p += 1
        # If the hexagonal number is less than the triangle or pentagonal, increment h
        elif hexagonal_num < triangle_num or hexagonal_num < pentagonal_num:
            h += 1
        else:
            return triangle_num


if __name__ == "__main__":
    print(f"Problem 45: {compute()}")
