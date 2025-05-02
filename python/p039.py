# pylint: disable=line-too-long
"""
Problem 39: Integer Right Triangles

Problem Description:
If p is the perimeter of a right-angled triangle with integer sides {a, b, c}, 
there are exactly three solutions for p = 120: {20, 48, 52}, {24, 45, 51}, {30, 40, 50}.
For which value of p ≤ 1000, is the number of solutions maximized?

Answer: 840
"""

from utils import profiler


def perimeter(p: int) -> int:
    """
    Computes the number of distinct integer solutions (a, b, c) where a, b, c are 
    the sides of a right-angle triangle with integral sides, and the perimeter is equal to p.
    
    For each perimeter p, we check all possible values of a and b that satisfy the 
    equation a + b + c = p, where c is determined from the Pythagorean theorem a^2 + b^2 = c^2.

    Args:
        p (int): The perimeter of the triangle.

    Returns:
        int: The number of distinct solutions (a, b, c) for the given perimeter p.
    """
    solutions = 0
    for a in range(1, p // 2):
        for b in range(a, p // 2):
            c = p - a - b
            if a + b + c == p and a**2 + b**2 == c**2:
                solutions += 1
    return solutions


@profiler
def compute() -> int:
    """
    Finds the perimeter p ≤ 1000 that results in the maximum number of solutions for 
    integer right-angled triangles (a, b, c) where a + b + c = p and a^2 + b^2 = c^2.
    
    The function iterates through all possible values of p from 1 to 1000, computes the 
    number of solutions for each perimeter, and identifies the value of p with the maximum number 
    of solutions.

    Returns:
        int: The value of p ≤ 1000 with the maximum number of right-angle triangle solutions.
    """
    max_solutions = 0
    max_p = 0
    for p in range(1, 1001):
        solutions = perimeter(p)
        if solutions > max_solutions:
            max_solutions = solutions
            max_p = p

    return max_p


if __name__ == "__main__":
    print(f"Problem 39: {compute()}")
