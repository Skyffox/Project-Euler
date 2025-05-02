# pylint: disable=line-too-long
"""
Problem 57: Square Root Convergents

Problem description:
We are tasked with calculating fractions in the form of continued fractions for the square root of 2. 
For the first 1000 expansions, we need to count how many fractions contain a numerator with more digits than the denominator.

The general form for the expansion is:
    a(n) = a(n-1) + 2 * b(n-1)
    b(n) = b(n-1) + a(n-1)

Answer: 153
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes how many fractions in the continued fraction expansions for the square root of 2
    contain a numerator with more digits than the denominator for the first 1000 expansions.
    
    The formula for continued fraction expansions of the square root of 2 is used to generate 
    the successive fractions. The process continues for 1000 terms, and the count of fractions 
    where the numerator has more digits than the denominator is returned.
    
    Returns:
        int: The number of fractions where the numerator has more digits than the denominator.
    """
    c = 0

    # Starting values of numerator and denominator.
    above = 3
    below = 2

    for _ in range(1000):
        # Calculate new values of numerator and denominator.
        tmp = above
        above = above + 2 * below
        below = tmp + below

        # Check if the numerator has more digits than the denominator.
        if len(str(above)) > len(str(below)):
            c += 1

    return c


if __name__ == "__main__":
    print(f"Problem 57: {compute()}")
