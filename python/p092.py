# pylint: disable=line-too-long
"""
Problem 92: Square Digit Chains

Problem description:
A number chain is created by continuously adding the square of the digits of a number 
to form a new number, until it repeats. Find how many starting numbers below ten million 
will arrive at 89.

Answer: 8581146
"""

from utils import profiler


def square_digits(n: int) -> int:
    """
    Returns the sum of the squares of the digits of a given number.

    For example:
    - square_digits(9119) returns 1^2 + 1^2 + 9^2 + 9^2 = 1 + 1 + 81 + 81 = 164.
    
    Args:
        n (int): The number whose digits will be squared.

    Returns:
        int: The sum of the squares of the digits of n.
    """
    return sum(int(digit) ** 2 for digit in str(n))


@profiler
def compute() -> int:
    """
    Computes how many numbers below 10 million eventually reach 89 in their square digit chains.
    
    Uses memoization to avoid recalculating known chains.
    
    Returns:
        int: Count of numbers whose chain ends at 89.
    """
    known_to_89 = set()
    known_to_1 = set()

    def follows_chain_to_89(n: int) -> bool:
        """Determines whether a number ends in 89 by following the chain of square digit sums."""
        chain = set()
        while n != 1 and n != 89:
            if n in known_to_89:
                known_to_89.update(chain)
                return True
            if n in known_to_1:
                known_to_1.update(chain)
                return False
            chain.add(n)
            n = square_digits(n)

        if n == 89:
            known_to_89.update(chain)
            return True
        else:
            known_to_1.update(chain)
            return False

    return sum(1 for i in range(2, 10_000_000) if follows_chain_to_89(i))


if __name__ == "__main__":
    print(f"Problem 92: {compute()}")
