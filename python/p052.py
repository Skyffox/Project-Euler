# pylint: disable=line-too-long
"""
Problem 52 - Permuted Multiples

Problem description:
The task is to find the smallest positive integer, x, such that the numbers 
x, 2x, 3x, 4x, 5x, and 6x all contain the same digits, but possibly in a different order.

For example, the number 125874 and its multiples 2*125874 = 251748, 3*125874 = 377622, etc. 
contain exactly the same digits, but in a different order. We are asked to find the smallest x 
for which the numbers x, 2x, 3x, 4x, 5x, and 6x contain exactly the same digits.

Answer: 142857
"""

from utils import profiler


def same(x: int, a: int, b: int) -> bool:
    """
    Checks if a and b multiples of x have the same digits, 
    by comparing the sorted digits of a*x and b*x.
    
    Args:
        x (int): The number to check for multiples.
        a (int): The first multiplier.
        b (int): The second multiplier.
        
    Returns:
        bool: True if both multiples contain the same digits, False otherwise.
    """
    return sorted(str(a * x)) == sorted(str(b * x))


@profiler
def compute() -> int:
    """
    Finds the smallest positive integer `x` such that the numbers 
    `x`, `2x`, `3x`, `4x`, `5x`, and `6x` contain the same digits.
    
    Returns:
        int: The smallest integer `x` that satisfies the condition.
    """
    x = 125874 # Starting point (known from the problem statement)
    while True:
        if all(same(x, i, i+1) for i in range(1, 6)): # Check multiples 1x, 2x, ..., 6x
            return x
        x += 1 # Try the next integer


if __name__ == "__main__":
    print(f"Problem 52: {compute()}")
