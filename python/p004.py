# pylint: disable=line-too-long
"""
Problem 1: Find the largest palindrome made from the product of two 3-digit numbers.
Answer: 906609
Execution time: 0.0040s
"""

from utils import profiler


@profiler
def compute() -> int:
    """Find the largest palindrome"""
    thirdnumber = 0
    for number in range(1000, 100, -1):
        for secondnumber in range(number, 100, -1):
            product = number * secondnumber

            if product <= thirdnumber:
                break

            # Check if product is a palindrome
            if str(product) == str(product)[::-1]:
                thirdnumber = product

    return thirdnumber


if __name__ == "__main__":
    print(f"Problem 4: {compute()}")
