# pylint: disable=line-too-long
"""
Problem 43: Sub-string Divisibility

Problem Description:
We are asked to find the sum of all 0 to 9 pandigital numbers that satisfy a specific set of divisibility rules. 
A 0 to 9 pandigital number uses each digit from 0 to 9 exactly once. The divisibility conditions are:
1. The number formed by digits 2-4 (inclusive) must be divisible by 2.
2. The number formed by digits 3-5 (inclusive) must be divisible by 3.
3. The number formed by digits 4-6 (inclusive) must be divisible by 5.
4. The number formed by digits 5-7 (inclusive) must be divisible by 7.
5. The number formed by digits 6-8 (inclusive) must be divisible by 11.
6. The number formed by digits 7-9 (inclusive) must be divisible by 13.
7. The number formed by digits 8-10 (inclusive) must be divisible by 17.

We need to find all such pandigital numbers and calculate their sum.

Answer: 16695334890
"""

import itertools
from typing import Tuple
from utils import profiler


def check_substring_divisibility(digits: Tuple[int, int, int, int, int, int, int, int, int, int]) -> bool:
    """
    Checks the divisibility rules for a given 0-9 pandigital number.
    
    The number is checked for the following substring divisibility conditions:
    1. Digits 2-4 divisible by 2
    2. Digits 3-5 divisible by 3
    3. Digits 4-6 divisible by 5
    4. Digits 5-7 divisible by 7
    5. Digits 6-8 divisible by 11
    6. Digits 7-9 divisible by 13
    7. Digits 8-10 divisible by 17
    
    Args:
        digits (tuple): A tuple representing the digits of the 0-9 pandigital number.
        
    Returns:
        bool: True if the number satisfies all divisibility conditions, otherwise False.
    """
    # Check each condition
    return (int(''.join(digits[1:4])) % 2 == 0 and
            int(''.join(digits[2:5])) % 3 == 0 and
            int(''.join(digits[3:6])) % 5 == 0 and
            int(''.join(digits[4:7])) % 7 == 0 and
            int(''.join(digits[5:8])) % 11 == 0 and
            int(''.join(digits[6:9])) % 13 == 0 and
            int(''.join(digits[7:10])) % 17 == 0)


@profiler
def compute():
    """
    Finds the sum of all 0 to 9 pandigital numbers that satisfy the given divisibility property.
    
    The divisibility property is checked for all permutations of the digits 0-9, where the number formed 
    by each permutation must satisfy specific substring divisibility rules.
    
    Returns:
        int: The sum of all pandigital numbers that meet the divisibility conditions.
    """
    # Generate all pandigital numbers (permutations of '0123456789')
    pandigital_nums = itertools.permutations('0123456789')

    total_sum = 0
    for num in pandigital_nums:
        if check_substring_divisibility(num):
            total_sum += int(''.join(num))  # Convert tuple to int and add to sum

    return total_sum


if __name__ == "__main__":
    print(f"Problem 43: {compute()}")
