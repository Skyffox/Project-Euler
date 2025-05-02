# pylint: disable=line-too-long
"""
Problem 88: Product-sum numbers

Problem description:
A natural number N can be written as the sum and product of a set of at least two natural numbers. Such a number is called a product-sum number. For example:
    6 = 1 + 2 + 3 = 1 * 2 * 3
The task is to find the sum of all distinct minimum product-sum numbers for all values of k ≥ 2. 
For each k, minSumProduct[k] is the smallest number that can be expressed as both the sum and the product of exactly k positive integers.

Answer: 7587457
"""

from utils import profiler


LIMIT = 12000
minsumproduct = [None] * (LIMIT + 1)


def factorize(n: int, remainder: int, maxfactor: int, current_sum: int, terms: int) -> None:
    """
    Factorizes the integer `n` and updates the minSumProduct for terms 
    that can represent both the sum and the product of `k` integers.

    Args:
    - n (int): The number being factorized.
    - remainder (int): The remaining product to be factored.
    - maxfactor (int): The maximum factor to consider.
    - current_sum (int): The current sum of factors.
    - terms (int): The number of terms used in the factorization.
    """
    if remainder == 1:
        if current_sum > n:
            raise AssertionError("Sum should never exceed the number.")
        terms += n - current_sum
        if terms <= LIMIT and (minsumproduct[terms] is None or n < minsumproduct[terms]):
            minsumproduct[terms] = n
    else:
        for i in range(2, maxfactor + 1):
            if remainder % i == 0:
                factor = i
                factorize(n, remainder // factor, min(factor, maxfactor), current_sum + factor, terms + 1)


@profiler
def compute() -> int:
    """
    Computes the sum of the distinct values of minSumProduct[k] for k >= 2.
    For each k, the smallest number N that can be expressed as both 
    a sum and a product of k positive integers is determined.

    Returns:
    	int: The sum of all distinct minSumProduct[k] for k >= 2.
    """
    # Iterate through all numbers from 2 to LIMIT * 2 and find their factorization
    for i in range(2, LIMIT * 2 + 1):
        factorize(i, i, i, 0, 0)

    # Eliminate duplicates and compute the sum of distinct minSumProduct values
    return sum(set(minsumproduct[2:]))


if __name__ == "__main__":
    print(f"Problem 88: {compute()}")
