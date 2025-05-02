# pylint: disable=line-too-long
"""
Problem 61: Cyclical Figurate Numbers

Problem description:
This module solves the problem of finding the sum of the only ordered set of six cyclic 
4-digit numbers for which each polygonal type: triangle, square, pentagonal, hexagonal, 
heptagonal, and octagonal, is represented by a different number in the set.

The solution involves generating polygonal numbers of each type and finding a set of numbers 
such that the last two digits of one number match the first two digits of the next number in the 
set, ultimately creating a cyclic sequence.

Answer: 28684
"""

from typing import Tuple, List, Dict
from utils import profiler


def triangle(n: int) -> int:
    """
    Generates the nth triangle number.
    
    Args:
        n (int): The index of the triangle number.

    Returns:
        int: The nth triangle number.
    """
    return n * (n + 1) // 2


def square(n: int) -> int:
    """
    Generates the nth square number.
    
    Args:
        n (int): The index of the square number.

    Returns:
        int: The nth square number.
    """
    return n ** 2


def pentagonal(n: int) -> int:
    """
    Generates the nth pentagonal number.
    
    Args:
        n (int): The index of the pentagonal number.

    Returns:
        int: The nth pentagonal number.
    """
    return n * (3 * n - 1) // 2


def hexagonal(n: int) -> int:
    """
    Generates the nth hexagonal number.
    
    Args:
        n (int): The index of the hexagonal number.

    Returns:
        int: The nth hexagonal number.
    """
    return n * (2 * n - 1)


def heptagonal(n: int) -> int:
    """
    Generates the nth heptagonal number.
    
    Args:
        n (int): The index of the heptagonal number.

    Returns:
        int: The nth heptagonal number.
    """
    return n * (5 * n - 3) // 2


def octagonal(n: int) -> int:
    """
    Generates the nth octagonal number.
    
    Args:
        n (int): The index of the octagonal number.

    Returns:
        int: The nth octagonal number.
    """
    return n * (3 * n - 2)


def generate_polygonal_numbers() -> Tuple[List[int], Dict[str, List[int]]]:
    """
    Generates all the polygonal numbers for each type that are four-digit numbers.

    Returns:
        tuple: A tuple containing:
            - List of triangle numbers (four-digit numbers).
            - Dictionary with polygonal number types (keys) and their corresponding four-digit numbers (values).
    """
    tri = [triangle(x) for x in range(45, 141)]
    squares = [square(x) for x in range(32, 100)]
    penta = [pentagonal(x) for x in range(26, 82)]
    hexa = [hexagonal(x) for x in range(23, 71)]
    hepta = [heptagonal(x) for x in range(21, 64)]
    octa = [octagonal(x) for x in range(19, 59)]

    return tri, {
        'square': squares,
        'pentagonal': penta,
        'hexagonal': hexa,
        'heptagonal': hepta,
        'octagonal': octa
    }


def find_candidates(num: int, indices: List[int], all_numbers: Dict[str, List[int]]) -> List[List[int]]:
    """
    Finds candidates for the next number in the cyclic sequence that match the last two digits 
    of the current number and the first two digits of a number from another polygonal type.
    
    Args:
        num (int): The current number in the sequence.
        indices (list): The list of already used polygonal number types (by index).
        all_numbers (dict): Dictionary containing the polygonal number lists.

    Returns:
        list: A list of candidate numbers and their polygonal type indices.
    """
    last_digits = [int(x) for x in str(num)][2:]
    candidates = []

    for idx, lst in enumerate(all_numbers.values()):
        if idx in indices:
            continue
        for n in lst:
            first_digits = [int(x) for x in str(n)][:2]
            if first_digits == last_digits:
                candidates.append([n, idx])

    return candidates


def find_cyclic_set(triangles: List[int], all_numbers: Dict[str, List[int]]) -> List[int]: 
    """
    Finds the cyclic set of polygonal numbers that satisfy the problem's condition.

    Args:
        triangles (list): List of triangle numbers.
        all_numbers (dict): Dictionary containing the polygonal number lists.

    Returns:
        list: A list of numbers that form the cyclic set.
    """
    for t in triangles:
        candidates = find_candidates(t, [], all_numbers)
        idx_lst = []

        for c1 in candidates:
            n1 = find_candidates(c1[0], idx_lst, all_numbers)
            if len(n1) == 0 or c1[1] in idx_lst:
                continue

            for c2 in n1:
                idx_lst = [c1[1]]
                n2 = find_candidates(c2[0], idx_lst, all_numbers)
                if len(n2) == 0 or c2[1] in idx_lst:
                    continue

                for c3 in n2:
                    idx_lst = [c1[1], c2[1]]
                    n3 = find_candidates(c3[0], idx_lst, all_numbers)
                    if len(n3) == 0 or c3[1] in idx_lst:
                        continue

                    for c4 in n3:
                        idx_lst = [c1[1], c2[1], c3[1]]
                        n4 = find_candidates(c4[0], idx_lst, all_numbers)
                        if len(n4) == 0 or c4[1] in idx_lst:
                            continue

                        for c5 in n4:
                            idx_lst = [c1[1], c2[1], c3[1], c4[1]]
                            if c5[1] in idx_lst:
                                continue

                            first_digits = [int(x) for x in str(t)][:2]
                            last_digits = [int(x) for x in str(c5[0])][2:]

                            if first_digits == last_digits:
                                return [t, c1[0], c2[0], c3[0], c4[0], c5[0]]

    return []


@profiler
def compute() -> int:
    """
    Computes the sum of the only ordered set of six cyclic 4-digit numbers for which each 
    polygonal type: triangle, square, pentagonal, hexagonal, heptagonal, and octagonal, 
    is represented by a different number in the set.

    Returns:
        int: The sum of the cyclic set of polygonal numbers.
    """
    triangles, all_numbers = generate_polygonal_numbers() # Generate all the polygonal numbers
    return sum(find_cyclic_set(triangles, all_numbers)) # Find the cyclic set


if __name__ == "__main__":
    print(f"Problem 61: {compute()}")
