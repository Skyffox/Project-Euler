# pylint: disable=line-too-long
"""
Problem 62: Cubic Permutations

Problem description:
In this problem, we are tasked with finding the smallest cube for which exactly five permutations of its digits are also cubes.
The goal is to efficiently find the smallest cube that has exactly five permutations of its digits that are also cubes.

Answer: 127035954683
"""

import collections
from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the smallest cube for which exactly five permutations of its digits are cubes.

    Returns:
        int: The smallest cube with exactly five permutations of its digits being cubes.
    """
    # Create a dictionary to store cubes by their sorted digits
    cubes_by_digits = collections.defaultdict(list)

    # Start checking cubes from cube of numbers
    n = 1
    while True:
        cube = n**3
        sorted_digits = ''.join(sorted(str(cube))) # Create the digit signature

        # Add this cube to the list of cubes with the same sorted digit signature
        cubes_by_digits[sorted_digits].append(cube)

        # Check if we have exactly 5 cubes with the same signature
        if len(cubes_by_digits[sorted_digits]) == 5:
            return min(cubes_by_digits[sorted_digits]) # Return the smallest cube

        n += 1 # Increment n to check the next cube


if __name__ == "__main__":
    print(f"Problem 62: {compute()}")
