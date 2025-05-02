# pylint: disable=line-too-long
"""
Problem 44: Pentagon Numbers

Problem Description:
The goal of the problem is to find a pair of pentagonal numbers (Pj, Pk) such that their sum 
and difference are both pentagonal numbers. The task is to find the minimized difference D = |Pk − Pj|.

The formula for pentagonal numbers is given as:
    P_n = n(3n - 1) / 2

We need to find the smallest difference D where both the sum and the difference of two pentagonal numbers 
are also pentagonal numbers.

Answer: 5482660
"""

from utils import profiler


def pentagonal_number(n: int) -> int:
    """
    Calculate the nth pentagonal number using the formula P_n = n(3n - 1) / 2.
    
    Args:
        n (int): The index of the pentagonal number.
        
    Returns:
        int: The nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


@profiler
def compute() -> int:
    """
    Find the pair of pentagonal numbers (Pj, Pk) such that their sum and difference are both pentagonal,
    and the difference D = |Pk − Pj| is minimized.
    
    Args:
        limit (int): The upper limit for generating pentagonal numbers.
        
    Returns:
        int: The minimized difference D.
    """
    # Set a reasonable limit for pentagonal numbers
    limit = 10000
    pentagonal_numbers = set(pentagonal_number(i) for i in range(1, limit))
    min_difference = float('inf')

    for i in range(1, limit):
        pj = pentagonal_number(i)
        for j in range(i+1, limit):
            pk = pentagonal_number(j)
            sum_p = pj + pk
            diff_p = abs(pk - pj)

            # Check if both sum and difference are pentagonal numbers
            if sum_p in pentagonal_numbers and diff_p in pentagonal_numbers:
                min_difference = min(min_difference, diff_p)

    return min_difference


if __name__ == "__main__":
    print(f"Problem 44: {compute()}")
