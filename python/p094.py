# pylint: disable=line-too-long
"""
Project Euler Problem 94: Almost Equilateral Triangles

Problem description:
An almost equilateral triangle is a triangle with side lengths (a, a, c), where c is either a+1 or a-1.
The height of the triangle can be computed using a right triangle with half the base (c/2) and side length a as the hypotenuse.

To produce a valid integer area, both the height (h) and half the base (c/2) must be integers, and (h, c/2, a) must be a Pythagorean triple.

Find the sum of the perimeters of all almost equilateral triangles with integer areas and perimeter ≤ 1,000,000,000.

Answer: 518408346
"""

import math
import itertools
from utils import profiler


@profiler
def compute():
    """
    This function calculates the sum of the perimeters of all almost equilateral 
    triangles with integer side lengths, where the perimeter does not exceed LIMIT (10^9).
    These triangles have side lengths in the form of (c, c, c +/- 1), where c is the integer 
    hypotenuse, and a^2 + b^2 = c^2 holds for the right triangle formed by splitting the 
    equilateral triangle down the middle.

    The solution uses primitive Pythagorean triples and iterates over possible values of 
    s and t that generate valid triples. It checks for the condition that either a*2 = c - 1 or 
    a*2 = c + 1 or the same conditions with b.

    Returns:
        str: The total sum of the perimeters of all valid almost equilateral triangles with integer sides
             where the perimeter does not exceed 10^9.
    """
    limit = 10**9
    total_perimeter = 0

    # We want to limit the search space based on the constraint:
    # 3c +/- 1 <= LIMIT, where c = (s^2 + t^2) / 2
    # This means we need to ensure 3s^2 - 1 <= LIMIT, i.e., s^2 <= (LIMIT + 1) / 3.
    for s in itertools.count(1, 2):  # s starts from 1 and increments by 2 (odd numbers only)
        if s * s > (limit + 1) // 3:
            break  # Stop if s^2 exceeds the limit

        # Iterate over possible t values (also odd), ensuring s > t > 0 and gcd(s, t) == 1
        for t in range(s - 2, 0, -2):  # t must be less than s, and t must be odd
            if math.gcd(s, t) == 1:  # Ensure s and t are coprime
                a = s * t
                b = (s * s - t * t) // 2
                c = (s * s + t * t) // 2

                # Check if a*2 = c - 1 or a*2 = c + 1
                if a * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= limit:
                        total_perimeter += p

                if a * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= limit:
                        total_perimeter += p

                # Check for the case where b*2 = c - 1 or b*2 = c + 1
                if b * 2 == c - 1:
                    p = c * 3 - 1
                    if p <= limit:
                        total_perimeter += p

                if b * 2 == c + 1:
                    p = c * 3 + 1
                    if p <= limit:
                        total_perimeter += p

    # Return the total perimeter as a string
    return str(total_perimeter)


if __name__ == "__main__":
    print(f"Problem 94: {compute()}")
