# pylint: disable=line-too-long
"""
Problem 90: Cube digit pairs

Problem description:
We are given two dice, each with 6 faces numbered from 0 to 9, and we want to determine 
how many valid arrangements of the dice there are, based on the conditions specified in 
the problem description.

Answer: 1217
"""

from utils import profiler


def popcount(x: int) -> int:
    """
    Returns the number of 1's in the binary representation of x (Hamming weight).
    
    Args:
        x (int): The integer whose binary representation will be counted for 1's.
        
    Returns:
        int: The number of 1's in the binary representation of x.
    """
    return bin(x).count("1")


def is_arrangement_valid(a: int, b: int) -> bool:
    """
    Checks whether two dice arrangements (represented as 10-bit numbers) are valid based
    on the rules of the problem. The dice must include faces 6 and 9, and all square digit
    pairs must match.

    Args:
        a (int): The 10-bit number representing the first die.
        b (int): The 10-bit number representing the second die.
        
    Returns:
        bool: True if the dice arrangements are valid, False otherwise.
    """
    # Ensure faces 6 and 9 are always included in both dice
    if test_bit(a, 6) or test_bit(a, 9):
        a |= (1 << 6) | (1 << 9)
    if test_bit(b, 6) or test_bit(b, 9):
        b |= (1 << 6) | (1 << 9)

    # Verify that all square pairs match between the dice
    return all(
        (test_bit(a, c) and test_bit(b, d)) or (test_bit(a, d) and test_bit(b, c))
        for c, d in SQUARES
    )


def test_bit(x: int, i: int) -> bool:
    """
    Checks if the i-th bit of the integer x is set (i.e., x has the corresponding face).

    Args:
        x (int): The integer representing a die.
        i (int): The bit position to check (corresponding to the die face).
        
    Returns:
        bool: True if the i-th bit of x is set, False otherwise.
    """
    return (x >> i) & 1 != 0


@profiler
def compute() -> str:
    """
    Computes the number of valid dice arrangements where each arrangement corresponds
    to a valid configuration of the dice based on the specified conditions.

    Returns:
        str: The number of valid dice arrangements as a string.
    """
    ans = sum(
        1
        for i in range(1 << 10) # Iterate over all 10-bit binary numbers (representing dice faces)
        for j in range(i, 1 << 10) # Ensures i <= j to avoid counting duplicates
        if popcount(i) == popcount(j) == 6 and is_arrangement_valid(i, j)
    )
    return str(ans)


# List of pairs of digits corresponding to square numbers
SQUARES = [(i**2 // 10, i**2 % 10) for i in range(1, 10)]


if __name__ == "__main__":
    print(f"Problem 90: {compute()}")
