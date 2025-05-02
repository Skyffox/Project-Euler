# pylint: disable=line-too-long
"""
Problem 99: Largest Exponentiation

Problem description:
Comparing the numbers a^b (where a and b are given for each line), 
determine which line number has the greatest numerical value. Since the numbers 
can be extremely large, we use logarithms to simplify the comparison.

Answer: The line number which contains the largest value of a^b.
"""

import math
from utils import profiler

@profiler
def compute() -> int:
    """
    Computes the line number of the largest exponentiation a^b from the input file.

    Reads each pair (a, b) from the file and compares their logarithmic values
    to determine which line yields the largest result.

    Returns:
        int: 1-based line number of the largest value.
    """
    best_line = 1
    max_value = float('-inf')

    with open("inputs/p099_base_exp.txt", "r", encoding="utf-8") as file:
        for idx, line in enumerate(file, start=1):
            base_str, exp_str = line.strip().split(",")
            base = int(base_str)
            exp = int(exp_str)

            # Use logarithms to avoid computing huge powers
            value = exp * math.log(base)

            if value > max_value:
                max_value = value
                best_line = idx

    return best_line

if __name__ == "__main__":
    print(f"Problem 99: {compute()}")
