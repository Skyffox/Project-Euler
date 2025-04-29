# pylint: disable=line-too-long
"""
Problem 109: In the game of darts a player throws three darts at a target board which is split into twenty equal sized sections numbered one to twenty.
             When a player is able to finish on their current score it is called a "checkout" and the highest checkout is 170: T20 T20 D25 (two treble 20s and double bull).
             How many distinct ways can a player checkout with a score less than 100?
Answer: 38182
Execution time: 0.9294s
"""

from utils import profiler


@profiler
def compute():
    """Calculate for every possible checkout how we may achieve that in 1, 2 or 3 throws (since singles contains a zero throw)"""
    singles = [("S" + str(i), i) for i in range(0, 21)] + [("S25", 25)]
    doubles = [("D" + str(i), 2*i) for i in range(1, 21)] + [("D50", 50)]
    triples = [("T" + str(i), 3*i) for i in range(1, 21)]

    # The maximum checkout is 170 and a player must finish with a double
    checkout = [[] for _ in range(171)]
    for (letter_1, dart_1) in singles + doubles + triples:
        for (letter_2, dart_2) in singles + doubles + triples:
            for (letter_3, dart_3) in doubles:
                total = dart_1 + dart_2 + dart_3
                # The first and second dart may be interchanged to form a solution, which is why we check for one solution and add the other.
                if (letter_2, letter_1, letter_3) not in checkout[total]:
                    checkout[total].append((letter_1, letter_2, letter_3))

    # Only interested in checkout scores with less than 100
    return sum([len(x) for x in checkout[:100]])


if __name__ == "__main__":
    print(f"Problem 109: {compute()}")
