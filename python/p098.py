# pylint: disable=line-too-long
"""
Problem 98: Anagramic Squares

Problem description:
Find the largest square number formed by any member of a pair of anagramic words.

Approach:
- Read and parse a word list to group anagram pairs.
- For each valid anagram pair, attempt all digit assignments.
- Check if the mapped words form valid square numbers.

Answer: 18769
"""

import math
from typing import Dict, List
from utils import profiler


def is_perfect_square(n: int) -> bool:
    """Returns True if n is a perfect square."""
    root = int(math.isqrt(n))
    return root * root == n


def try_digit_assignments(a: str, b: str, index: int, assignments: Dict[str, int], used_digits: List[bool]) -> int:
    """
    Recursively tries digit assignments to letters and checks if both words map to perfect squares.
    
    Args:
        a (str): First word in the anagram pair.
        b (str): Second word in the anagram pair.
        index (int): Current character index being assigned.
        assignments (dict): Current letter-to-digit assignments.
        used_digits (list): Boolean list to mark used digits.

    Returns:
        int: The maximum square number found for valid assignments; otherwise 0.
    """
    if index == len(a):
        if assignments[a[0]] == 0 or assignments[b[0]] == 0:
            return 0  # No leading zeros

        anum = int("".join(str(assignments[ch]) for ch in a))
        bnum = int("".join(str(assignments[ch]) for ch in b))

        if is_perfect_square(anum) and is_perfect_square(bnum):
            return max(anum, bnum)
        return 0

    char = a[index]
    if char in assignments:
        return try_digit_assignments(a, b, index + 1, assignments, used_digits)

    max_result = 0
    for digit in range(10):
        if not used_digits[digit]:
            used_digits[digit] = True
            assignments[char] = digit

            max_result = max(max_result, try_digit_assignments(a, b, index + 1, assignments, used_digits))

            used_digits[digit] = False
            del assignments[char]

    return max_result


@profiler
def compute() -> str:
    """
    Main function that solves Problem 98 by checking all anagram word pairs
    and finding the maximum square number that can be formed from them.

    Returns:
        str: The largest square number found as a string.
    """
    with open("inputs/p098_words.txt", "r", encoding="utf-8") as file:
        words = file.read().replace('"', '').split(',')

    # Group words by sorted characters to find anagram sets
    anagram_groups: Dict[str, List[str]] = {}
    for word in words:
        key = ''.join(sorted(word))
        anagram_groups.setdefault(key, []).append(word)

    max_square = 0

    # Check each group of anagram words
    for group in anagram_groups.values():
        if len(group) < 2:
            continue
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                max_square = max(
                    max_square,
                    try_digit_assignments(group[i], group[j], 0, {}, [False] * 10)
                )

    return str(max_square)

if __name__ == "__main__":
    print(f"Problem 98: {compute()}")
