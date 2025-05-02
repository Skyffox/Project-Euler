# pylint: disable=line-too-long
"""
Problem 36: Double-base Palindromes

Problem Description:
The decimal number, 585, is palindromic in both base 10 and base 2. Specifically: 585 in decimal is 1001001001 in binary (both are palindromes).
The task is to find the sum of all numbers less than one million that are palindromic in both base 10 and base 2.

Answer: 872187
"""

from utils import profiler


def is_palindrome(n: int) -> bool:
    """
    Checks whether a given number is a palindrome.
    A palindrome is a number that reads the same forward and backward.
    
    Args:
        n (int): The number to check for being a palindrome.

    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(n) == str(n)[::-1]


@profiler
def compute() -> int:
    """
    Computes the sum of all numbers less than one million that are palindromic in both base 10 and base 2.

    This function iterates over all numbers below one million, checks if they are palindromes in base 10,
    and then checks if their binary representation is also a palindrome. If both conditions are true,
    the number is added to the sum.

    Returns:
        int: The sum of all double-base palindromes below one million.
    """
    total = 0
    for x in range(1, 1000000):
        if is_palindrome(x): # Check if the number is a palindrome in base 10
            binary_rep = bin(x)[2:] # Get binary representation (without the '0b' prefix)
            if is_palindrome(binary_rep): # Check if the binary representation is also a palindrome
                total += x

    return total


if __name__ == "__main__":
    print(f"Problem 36: {compute()}")
