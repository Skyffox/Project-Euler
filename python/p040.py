# pylint: disable=line-too-long
"""
Problem 40: Champernowne's Constant

Problem Description:
An irrational decimal fraction is created by concatenating the positive integers: 0.123456789101112131415161718192021...
It can be seen that the 12th digit of the fractional part is 1.
The task is to find the product of the 1st, 10th, 100th, 1000th, 10000th, and 100000th digits in the fractional part of Champernowne's constant.

Answer: 210
"""

from utils import profiler


def champernowne(last: int) -> str:
    """
    Generates the decimal expansion of Champernowne's constant up to a specified number of digits.
    This function concatenates the numbers from 1 to `last` and returns the resulting string.
    
    Args:
        last (int): The last number to include in the sequence.
        
    Returns:
        str: The concatenated sequence of numbers from 1 to `last` as a string.
    """
    ans = ""
    for c in range(1, last + 1): # Start from 1, not 0, to match the problem's description
        ans += str(c)
    return ans


@profiler
def compute() -> int:
    """
    Computes the product of the 1st, 10th, 100th, 1000th, 10000th, and 100000th digits in Champernowne's constant.
    
    This function generates the Champernowne constant up to the required number of digits and multiplies the digits
    at positions 1, 10, 100, 1000, 10000, and 100000 in the decimal expansion.
    
    Returns:
        int: The product of the 1st, 10th, 100th, 1000th, 10000th, and 100000th digits.
    """
    champ = champernowne(200000) # Generate enough digits (up to 200,000th position)
    answer = 1

    # Multiply the digits at the required positions (1, 10, 100, 1000, 10000, 100000)
    for c in range(6):
        answer *= int(champ[10**c - 1]) # Subtract 1 because string indices are 0-based

    return answer


if __name__ == "__main__":
    print(f"Problem 40: {compute()}")
