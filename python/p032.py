# pylint: disable=line-too-long
"""
Problem 32: Pandigital Products

Problem description:
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital number.

The multiplicand, multiplier, and product identity can be written as a 1 through 9 pandigital if:
- The concatenation of the multiplicand, multiplier, and product contains all digits from 1 to 9 exactly once.

Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9 pandigital.

Answer: 45228
"""

from utils import profiler


def is_pandigital(multiplicand: int, multiplier: int, product: int) -> bool:
    """
    Checks if the concatenation of the multiplicand, multiplier, and product
    forms a 1 through 9 pandigital number.

    Args:
        multiplicand (int): The multiplicand of the equation.
        multiplier (int): The multiplier of the equation.
        product (int): The product of the multiplicand and multiplier.

    Returns:
        bool: True if the concatenated multiplicand, multiplier, and product
              forms a 1 through 9 pandigital number, else False.
    """
    combined = str(multiplicand) + str(multiplier) + str(product)

    # Check if the concatenated string has exactly the digits 1 through 9 once
    return sorted(combined) == ['1', '2', '3', '4', '5', '6', '7', '8', '9']


@profiler
def compute() -> int:
    """
    Computes the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital number.

    Returns:
        int: The sum of all the pandigital products.
    """
    pandigital_products = set()  # Using a set to store unique products

    # Iterate over possible multiplicands and multipliers
    for i in range(1, 50):  # First multiplicand should be less than 50
        for j in range(1, 2000):  # Second multiplier should be less than 2000
            product = i * j
            if is_pandigital(i, j, product):
                pandigital_products.add(product)

    return sum(pandigital_products)


if __name__ == "__main__":
    print(f"Problem 32: {compute()}")
