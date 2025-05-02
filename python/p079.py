# pylint: disable=line-too-long
"""
Problem 79: Passcode Derivation

Problem description:
Given a file containing a series of 3-digit numbers, where the digits are always in order, 
the task is to determine the shortest possible secret passcode of unknown length. 
The passcode is formed by determining the minimum sequence of digits required to satisfy the given constraints.

Answer: 73162890
"""

from utils import profiler


@profiler
def compute() -> str:
    """
    Analyzes the given input to determine the shortest possible secret passcode.
    
    Returns:
        str: The shortest possible passcode formed from the input.
    """
    # Open and read the input file
    with open('inputs/p079_keylog.txt', 'r', encoding="utf-8") as f:
        keys = [line.strip() for line in f]

    # Create a set of unique digits from the input
    all_digits = set(''.join(keys)) # All unique digits involved in the keys

    # Initialize a list of pairs representing constraints (e.g., first digit must come before second digit)
    constraints = []
    for key in keys:
        constraints.append([key[0], key[1]]) # first digit before second digit
        constraints.append([key[1], key[2]]) # second digit before third digit
        constraints.append([key[0], key[2]]) # first digit before third digit

    # Remove duplicate constraints
    constraints = [list(pair) for pair in set(map(tuple, constraints))]

    # Count how many times each digit is constrained to appear before another digit
    digit_order = {digit: 0 for digit in all_digits}
    for constraint in constraints:
        digit_order[constraint[1]] += 1

    # Sort digits based on the number of constraints (digits with fewer constraints come earlier)
    sorted_digits = sorted(digit_order.items(), key=lambda x: x[1])

    # The final passcode is the sorted sequence of digits based on the constraint analysis
    passcode = ''.join([digit[0] for digit in sorted_digits])

    return int(passcode)


if __name__ == "__main__":
    print(f"Problem 79: {compute()}")
