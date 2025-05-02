# pylint: disable=line-too-long
"""
Problem 71: Ordered Fractions

Problem description:
This module solves the problem of finding the numerator of the fraction immediately to the left of 3/7
when listing all reduced proper fractions for d ≤ 1,000,000 in ascending order of size.

A reduced proper fraction is one where the numerator and denominator are coprime (gcd(p, q) = 1).
The goal is to find the fraction just smaller than 3/7 with the denominator less than or equal to 1,000,000.

Approach:
1. Iterate over all values of q (denominator) from 1,000,000 down to 1.
2. For each q, calculate p = floor((3 * q - 1) / 7) to ensure the fraction is smaller than 3/7.
3. Ensure the fraction is reduced by checking that gcd(p, q) = 1.
4. Track the largest fraction smaller than 3/7, and return its numerator.

Answer: 428570
"""

import math
from utils import profiler

@profiler
def compute() -> int:
    """
    Finds the numerator of the fraction immediately to the left of 3/7 in the ordered list of 
    all reduced proper fractions with denominators less than or equal to 1,000,000.

    Returns:
        int: The numerator of the fraction immediately to the left of 3/7 with denominator ≤ 1,000,000.
    """
    # Given values for 3/7
    top = 3
    bot = 7
    limit = 1000000

    # Initialize variables to store the best fraction
    r = 0 # numerator of the best fraction
    s = 1 # denominator of the best fraction

    for q in range(limit, 0, -1):
        # Calculate the numerator p of the fraction p/q which is just smaller than 3/7
        p = (top * q - 1) // bot

        # Check if the fraction p/q is smaller than 3/7 and larger than the current best fraction
        if p * s > r * q and math.gcd(p, q) == 1:
            r = p # update the best numerator
            s = q # update the best denominator

    # Return the numerator of the fraction immediately to the left of 3/7
    return r


if __name__ == "__main__":
    print(f"Problem 71: {compute()}")
