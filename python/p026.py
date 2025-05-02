# pylint: disable=line-too-long
"""
Problem 26: Reciprocal Cycles

Problem description:
Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

Answer: 983
"""

from utils import profiler


@profiler
def compute() -> int:
    """    
    This function iterates through all values of d from 2 to 999, calculating the decimal expansion of 1/d
    and determining the length of its repeating cycle. The value of d with the longest cycle is returned.
    
    Returns:
        int: The value of d < 1000 that produces the longest recurring cycle in the decimal expansion of 1/d.
    """
    longest_cycle = 0
    max_d = 0

    for d in range(2, 1000):
        seen = {}
        value = 1
        position = 0

        while value != 0 and value not in seen:
            seen[value] = position
            value = (value * 10) % d
            position += 1

        cycle_length = position - seen.get(value, 0)
        if cycle_length > longest_cycle:
            longest_cycle = cycle_length
            max_d = d

    return max_d


if __name__ == "__main__":
    print(f"Problem 26: {compute()}")
