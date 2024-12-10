# pylint: disable=line-too-long
"""
Problem 1: By considering the terms in the Fibonacci sequence whose values do not
           exceed four million, find the sum of the even-valued terms.
Answer: 4613732
Execution time: 0.0000s
"""

from utils import profiler

@profiler
def fibonacci_numbers(limit: int) -> int:
    """Generate a list of Fibonacci numbers"""
    lst = [1, 2]
    first = 1
    second = 2
    third = first + second

    while third < limit:
        lst.append(third)
        first, second = second, third
        third = first + second

    return sum([x for x in lst if x % 2 == 0])


if __name__ == "__main__":
    print(f"Problem 2: {fibonacci_numbers(4000000)}")
