# pylint: disable=line-too-long
"""
Problem 109: Dartboard Checkout Combinations

Problem description:
In the game of darts, a player throws three darts at a target board which is divided into twenty equal-sized sections numbered 1 through 20.
A "checkout" refers to a combination of throws that allows a player to finish their current score. The highest checkout score is 170, achieved 
by the combination T20 T20 D25 (two treble 20s and a double bull).

The task is to determine how many distinct ways a player can achieve a checkout with a score of less than 100. 
A checkout can be made with 1, 2, or 3 darts, and it must end with a double.

Answer: 38182
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the number of distinct checkout combinations with a score less than 100.

    This function considers the possible ways to achieve every score from 0 to 99 by throwing darts in 1, 2, or 3 attempts.
    A checkout can consist of a combination of single, double, or triple scores, and it must end with a double.
    
    The function calculates all possible checkout combinations and counts the distinct ways to achieve each score.
    
    Returns:
        int: The number of distinct ways to achieve a checkout with a score less than 100.
    """
    # Define the possible single, double, and triple darts
    singles = [("S" + str(i), i) for i in range(0, 21)] + [("S25", 25)]
    doubles = [("D" + str(i), 2*i) for i in range(1, 21)] + [("D50", 50)]
    triples = [("T" + str(i), 3*i) for i in range(1, 21)]

    # Initialize a list to store the possible combinations for each score
    checkout = [[] for _ in range(171)]

    # Iterate over all possible combinations of singles, doubles, and triples
    for (letter_1, dart_1) in singles + doubles + triples:
        for (letter_2, dart_2) in singles + doubles + triples:
            for (letter_3, dart_3) in doubles:  # The last dart must be a double
                total = dart_1 + dart_2 + dart_3

                # Ensure each combination is unique, and prevent duplicate solutions
                if (letter_2, letter_1, letter_3) not in checkout[total]:
                    checkout[total].append((letter_1, letter_2, letter_3))

    # Only count combinations for scores less than 100
    return sum([len(x) for x in checkout[:100]])


if __name__ == "__main__":
    print(f"Problem 109: {compute()}")
