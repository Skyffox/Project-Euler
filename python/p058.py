# pylint: disable=no-name-in-module, line-too-long
"""
Problem 58: Spiral Primes

Problem description:
In this problem, we are tasked with finding the side length of a square spiral in which the 
ratio of prime numbers along both diagonals first falls below 10%. 

The spiral begins with the number 1 at the center, and numbers are added spirally in an 
anticlockwise direction. For each new layer of the spiral, numbers are placed along the 
diagonals. We need to track the prime numbers along the diagonals and stop when the ratio 
of primes to total diagonal numbers drops below 10%.

The solution computes the side length of the spiral at this point.

Answer: 26241
"""

from utils import profiler, is_prime


@profiler
def compute() -> int:
    """
    Finds the side length of the square spiral for which the ratio of primes along both 
    diagonals first falls below 10%.
    
    This function simulates the growth of the spiral, checks for primes on both diagonals, 
    and stops when the ratio of primes to total diagonal numbers is less than 10%.

    Returns:
        int: The side length of the square spiral when the ratio of primes drops below 10%.
    """
    c = 1 # Center value of the spiral (starting number)
    last_num = 9 # The last number on the current spiral layer
    width = 3 # Starting with a 3x3 spiral

    primes = 0 # Count of prime numbers on diagonals
    total = 1 # Total numbers on diagonals (starting with the center number 1)

    # Loop to generate spirals and check primes on diagonals
    while True:
        # Check the four diagonal numbers in the current layer of the spiral
        if is_prime(c + width - 1):
            primes += 1
        if is_prime(c + 2 * (width - 1)):
            primes += 1
        if is_prime(c + 3 * (width - 1)):
            primes += 1

        # Four new numbers on the diagonals
        total += 4

        # Check if the ratio of primes to total numbers falls below 10%
        if (primes / total) * 100 < 10:
            break

        # Move to the next layer of the spiral
        width += 2
        c = last_num
        last_num = width**2 # The next corner number of the new layer

    # Return the side length of the spiral when the prime ratio drops below 10%
    return width


if __name__ == "__main__":
    print(f"Problem 58: {compute()}")
