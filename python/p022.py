# pylint: disable=line-too-long
"""
Problem 22: Name Scores

Problem description:
Using names.txt work out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.
What is the total of all the name scores in the file?

Answer: 871198282
"""

from utils import profiler


def name_score(name: str) -> int:
    """
    Calculate the alphabetical value of a given name.

    The alphabetical value is calculated by summing the position of each letter
    in the alphabet (A = 1, B = 2, ..., Z = 26). For example, the name 'COLIN'
    has a score of 3 + 15 + 12 + 9 + 14 = 53.

    Args:
        name (str): The name to calculate the alphabetical score for.

    Returns:
        int: The total alphabetical value of the name.
    """
    return sum(ord(char) - ord('A') + 1 for char in name)


@profiler
def compute() -> int:
    """
    Compute the total of all name scores from a file of names.

    This function reads a file containing a list of names (in CSV format),
    calculates the alphabetical value for each name using the `name_score` function,
    and multiplies the score of each name by its position in the sorted list (1-based index).
    The final result is the sum of these weighted name scores.

    The names are read from the file 'inputs/p022_names.txt', sorted alphabetically,
    and the total name score is returned.

    Returns:
        int: The total sum of the name scores.
    """
    with open('inputs/p022_names.txt', encoding="utf-8") as f:
        names = sorted(f.read().replace('"', '').split(','))

    total = sum((i + 1) * name_score(name) for i, name in enumerate(names))
    return total


if __name__ == "__main__":
    print(f"Problem 22: {compute()}")
