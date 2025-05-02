# pylint: disable=line-too-long
"""
Problem 33: Digit Cancelling Fractions

Problem description:
The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, 
which is correct, obtained by cancelling the 9s. We shall consider fractions like 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator. 
If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

Answer: 100
"""

from typing import List
from utils import profiler


def gcd(a: int, b: int) -> int:
    """
    Calculates the greatest common divisor (GCD) of two integers using the Euclidean algorithm.

    Args:
        a (int): The first integer.
        b (int): The second integer.

    Returns:
        int: The greatest common divisor of a and b.
    """
    while b:
        a, b = b, a % b
    return a


def simplify(fractions: List[int]) -> int:
    """
    Simplifies a list of fractions by finding their product and reducing it to its lowest terms.

    Args:
        fractions (list): A list of tuples, where each tuple represents a fraction in the form (numerator, denominator).

    Returns:
        int: The denominator of the simplified product of fractions.
    """
    numerator = 1
    denominator = 1

    # Loop through each fraction in the list
    for frac in fractions:
        a, b = frac

        # Simplify the fraction by dividing by their GCD
        common_divisor = gcd(a, b)
        reduced_num = a // common_divisor
        reduced_den = b // common_divisor

        numerator *= reduced_num
        denominator *= reduced_den

    # Simplify the final product of fractions
    common_divisor = gcd(numerator, denominator)
    simplified_denominator = denominator // common_divisor

    return simplified_denominator


@profiler
def compute() -> int:
    """
    Computes the denominator of the product of all non-trivial digit cancelling fractions.

    Returns:
        int: The denominator of the simplified product of the fractions.
    """
    fractions = []

    # Generate all possible fractions (x/y) where x < y and both have two digits
    for x in range(10, 100):
        for y in range(10, 100):
            if x >= y:
                continue

            # Split the numerator and denominator into digits
            num_digits = list(str(x))
            denom_digits = list(str(y))

            num1, num2 = int(num_digits[0]), int(num_digits[1])
            denom1, denom2 = int(denom_digits[0]), int(denom_digits[1])

            # Check for digit cancellation: if the digit in numerator matches the digit in denominator
            if num2 == denom1 and denom2 > 0 and x / y == num1 / denom2:
                fractions.append([num1, denom2])

    # Simplify the fractions and return the denominator of the simplified product
    return simplify(fractions)


if __name__ == "__main__":
    print(f"Problem 33: {compute()}")
