# pylint: disable=line-too-long
"""
Problem 15: Lattice Paths

Problem description:
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

Answer: 137846528820
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Calculate the number of paths through a 20x20 grid using combinatorics.

    In a grid of size 20x20, to reach the bottom-right corner, you need to make exactly 
    20 moves down and 20 moves to the right. The total number of distinct paths is 
    equivalent to the number of ways to arrange a sequence of 20 downs (D) and 20 rights (R).
    This is a combinatorial problem, where the result is given by the binomial coefficient 
    C(40, 20), representing the number of ways to choose 20 moves (down or right) from a total of 40 moves.

    Returns:
        int: The number of distinct paths through the 20x20 grid.
    """
    n = 2 * 20
    k = 20

    # Compute the binomial coefficient using the multiplicative formula
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)

    return result


if __name__ == "__main__":
    print(f"Problem 15: {compute()}")
