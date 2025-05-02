# pylint: disable=line-too-long
"""
Problem 4: Largest palindrome product

Problem description:
Find the largest palindrome made from the product of two 3-digit numbers.

Answer: 906609
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Finds the largest palindrome made from the product of two 3-digit numbers.

    This function iterates through the range of 3-digit numbers, computes the product
    of each pair, and checks if the product is a palindrome. The largest palindrome
    is returned.

    Returns:
        int: The largest palindrome made from the product of two 3-digit numbers.
    """
    largest_palindrome = 0

    # Iterate over the range of 3-digit numbers (from 999 down to 100)
    for number in range(999, 99, -1):
        for second_number in range(number, 99, -1):
            product = number * second_number

            # If the product is smaller than the largest palindrome, no need to continue
            if product <= largest_palindrome:
                break

            # Check if the product is a palindrome
            if str(product) == str(product)[::-1]:
                largest_palindrome = product

    return largest_palindrome


if __name__ == "__main__":
    print(f"Problem 4: {compute()}")
