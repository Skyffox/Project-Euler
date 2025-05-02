"""
Problem 100: Arranged probabilities
-----------------------------------
In a box, there are blue and red discs. A player draws two blue discs from the box. 
The probability of selecting two blue discs is:

    b / (b + r) * (b - 1) / (b + r - 1) = 1 / 2,

where `b` represents the number of blue discs and `r` represents the number of red discs. 
We are tasked with finding the smallest number of blue discs `b` such that the total number 
of discs `b + r` exceeds 10^12 and the probability of selecting two blue discs is exactly 1/2.

Answer: 756872327473
"""

import math
from utils import profiler

@profiler
def compute():
    """
    This function finds the number of blue discs (b) for the first solution to the equation 
    derived from the probability condition where the total number of discs (blue + red) exceeds 
    10^12, and the probability of selecting two blue discs is exactly 1/2.
    
    The problem is formulated as a Pell's equation: x^2 - 8y^2 = 1. Using the fundamental 
    solution to this equation (x0, y0) = (3, 1), we can generate successive solutions 
    and check when the sum of blue and red discs exceeds 10^12.
    
    Returns:
        str: The number of blue discs for the first valid solution.
    """
    # Fundamental solution to the Pell's equation
    x0 = 3
    y0 = 1

    # Current solution for x (blue discs) and y (red discs)
    x = x0
    y = y0  # The number of red discs

    while True:
        # Check if the solution satisfies the required condition
        sqrt = math.isqrt(y**2 * 8 + 1)

        # Check if the square root is odd (for the solution to be valid)
        if sqrt % 2 == 1:  # It must be odd
            # Calculate the number of blue discs
            blue = (sqrt + 1) // 2 + y

            # Check if the total number of discs exceeds 10^12
            if blue + y > 10**12:
                return str(blue)

        # Generate the next solution using the recurrence relations
        nextx = x * x0 + y * y0 * 8
        nexty = x * y0 + y * x0
        x = nextx
        y = nexty


if __name__ == "__main__":
    print(f"Problem 100: {compute()}")
