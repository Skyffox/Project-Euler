# pylint: disable=line-too-long
"""
Project Euler Problem 91: Right triangles with integer coordinates

Problem description:
We are tasked with determining how many right-angled triangles can be formed with integer 
coordinates (x1, y1) and (x2, y2), where the right angle is at the origin (0, 0). The goal 
is to count how many such triangles satisfy the given conditions, with coordinates in the range [0, 50].

Answer: 14234
"""

from utils import profiler

@profiler
def compute() -> str:
    """
    Computes the number of valid right-angled triangles with integer coordinates (x1, y1) and (x2, y2)
    that have their right angle at the origin (0, 0). The coordinates of the points (x1, y1) and (x2, y2)
    must be within a specified limit and satisfy the conditions for forming a right triangle.

    Returns:
        str: The number of valid right-angled triangles as a string.
    """
    LIMIT = 51  # Points are within the range 0 to 50 inclusive
    ans = sum(
        1
        for x1 in range(LIMIT)
        for y1 in range(LIMIT)
        for x2 in range(LIMIT)
        for y2 in range(LIMIT)
        # Ensure that (x1, y1) forms a larger angle than (x2, y2) for uniqueness
        if y2 * x1 < y1 * x2 and is_right_triangle(x1, y1, x2, y2)
    )
    return str(ans)


def is_right_triangle(x1: int, y1: int, x2: int, y2: int) -> bool:
    """
    Determines whether the three points (0, 0), (x1, y1), and (x2, y2) form a right-angled triangle.

    Args:
        x1 (int): x-coordinate of the first point.
        y1 (int): y-coordinate of the first point.
        x2 (int): x-coordinate of the second point.
        y2 (int): y-coordinate of the second point.

    Returns:
        bool: True if the points form a right-angled triangle, False otherwise.
    """
    a = x1**2 + y1**2  # Square of the distance from (0, 0) to (x1, y1)
    b = x2**2 + y2**2  # Square of the distance from (0, 0) to (x2, y2)
    c = (x2 - x1)**2 + (y2 - y1)**2  # Square of the distance between the points (x1, y1) and (x2, y2)

    # Check if any of the Pythagorean theorem conditions are satisfied (a^2 + b^2 = c^2)
    return (a + b == c) or (b + c == a) or (c + a == b)

if __name__ == "__main__":
    print(f"Problem 91: {compute()}")
