# pylint: disable=line-too-long
"""
Problem 66: Diophantine Equation

Problem description:
This module solves the Diophantine equation of the form x^2 - Dy^2 = 1, known as Pell's equation,
for values of D up to a given limit (in this case, D ≤ 1000). The goal is to find the value of D
that produces the largest solution for x.

Answer: 661
"""

import math
from utils import profiler


def is_perfect_square(n: int) -> bool:
    """
    Checks if a given number is a perfect square.

    Args:
        n (int): The number to check.

    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    return int(math.isqrt(n))**2 == n


def solve_pells_equation(D: int) -> int:
    """
    Solves Pell's equation x^2 - Dy^2 = 1 for a given non-perfect-square D
    using continued fraction expansion to find the minimal solution (x, y).

    Args:
        D (int): The value for which Pell's equation is solved.

    Returns:
        int or None: The minimal value of x that satisfies the equation, or None if no solution exists (D is a perfect square).
    """
    m, d, a = 0, 1, int(math.isqrt(D))
    if a * a == D:
        return None # No solution if D is a perfect square

    num1, num2 = 1, a
    denom1, denom2 = 0, 1

    # Using continued fraction expansion method
    while num2 * num2 - D * denom2 * denom2 != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (int(math.isqrt(D)) + m) // d
        num1, num2 = num2, a * num2 + num1
        denom1, denom2 = denom2, a * denom2 + denom1

    return num2 # Return the minimal x


@profiler
def compute() -> int:
    """
    Finds the value of D that produces the largest solution for x in Pell's equation 
    x^2 - Dy^2 = 1 for D ≤ limit.

    Returns:
        int: The value of D that produces the largest x.
    """
    limit = 1000  # Set the upper bound for D
    max_x = 0
    best_d = 0

    for D in range(2, limit + 1):
        if not is_perfect_square(D):
            x = solve_pells_equation(D)
            if x and x > max_x:
                max_x = x
                best_d = D

    return best_d


if __name__ == "__main__":
    print(f"Problem 66: {compute()}")
