# pylint: disable=line-too-long
"""
Problem 9: Special Pythagorean triplet

Problem description:
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

Answer: 31875000
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Finds the product of the Pythagorean triplet (a, b, c) such that a + b + c = 1000 
    and a^2 + b^2 = c^2.

    Returns:
        int: The product abc of the Pythagorean triplet.
    """
    limit = 1000

    # Iterate over possible values of c and b to find the triplet
    for c in range(1, limit):
        for b in range(1, c):
            a = limit - c - b  # Calculate a based on the constraint a + b + c = 1000
            if a**2 + b**2 == c**2:  # Check if it's a Pythagorean triplet
                return a * b * c


if __name__ == "__main__":
    print(f"Problem 9: {compute()}")
