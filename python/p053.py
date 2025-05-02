# pylint: disable=line-too-long
"""
Problem 53 - Combinatoric Selections

Problem description:
The task is to find how many combinations, C(n, r), for 1 <= n <= 100 are greater than one million. 
A combination is defined as C(n, r) = n! / (r!(n - r)!), where n! is the factorial of n. 
The goal is to count how many values of C(n, r) exceed one million for 1 <= n <= 100 and 0 <= r <= n.

Answer: 4075
"""

from utils import profiler


def factorial(n: int) -> int:
    """
    Computes the factorial of a number n iteratively.

    The factorial of a number n (denoted as n!) is the product of all positive integers 
    less than or equal to n. This function computes the factorial in an iterative manner 
    to avoid potential issues with recursion depth limits.

    Args:
        n (int): A non-negative integer for which the factorial is to be computed.

    Returns:
        int: The factorial of the number n.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def combinatorics(n: int, r: int) -> int:
    """
    Computes the combination C(n, r) using precomputed factorial values.

    The combination C(n, r) represents the number of ways to choose r elements from a set 
    of n elements without regard to the order of selection. The formula for the combination is:
    C(n, r) = n! / (r!(n - r)!). This function utilizes precomputed factorials for efficient calculation.

    Args:
        n (int): The total number of elements in the set.
        r (int): The number of elements to choose from the set.
        
    Returns:
        int: The combination C(n, r).
    """
    return factorial(n) / (factorial(r) * factorial(n - r))


@profiler
def compute() -> int:
    """
    Finds how many combinations C(n, r) for 1 <= n <= 100 are greater than one million.

    This function iterates through all values of n (from 1 to 100) and r (from 0 to n), 
    computing the combinations using precomputed factorials. It counts how many of these 
    combinations are greater than one million.

    Returns:
        int: The number of combinations C(n, r) for 1 <= n <= 100 that are greater than one million.
    """
    vals = 0
    for n in range(1, 101):
        for r in range(n + 1):
            if combinatorics(n, r) > 1000000:
                vals += 1
    return vals


if __name__ == "__main__":
    print(f"Problem 53: {compute()}")
