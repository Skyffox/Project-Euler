# pylint: disable=line-too-long
"""
Problem 15: Starting in the top left corner of a 2×2 grid, and only being able to move to
            the right and down, there are exactly 6 routes to the bottom right corner.
            How many such routes are there through a 20×20 grid?
Answer: 
Execution time: 0.0000s
"""

from utils import profiler


def binomial_coefficient(n, k):
    """Compute the binomial coefficient"""
    # Ensure k is the smaller of n - k and k for efficiency
    k = min(k, n - k)

    # Compute the binomial coefficient using the multiplicative formula
    result = 1
    for i in range(k):
        result *= (n - i)
        result //= (i + 1)

    return result


@profiler
def compute():
    """
    The number of paths through an n x n grid is a combinatorial problem. At each step, you have to either move down or right. 
    To get to the bottom-right corner, you need to make exactly 20 moves down and 20 moves to the right. Thus, the problem boils 
    down to finding the number of ways to arrange a sequence of 20 downs (D) and 20 rights (R).
    """
    return binomial_coefficient(2 * 20, 20)


if __name__ == "__main__":
    print(f"Problem 15: {compute()}")
