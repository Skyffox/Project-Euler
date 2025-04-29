# pylint: disable=line-too-long
"""
Problem 112: Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number; for example, 134468.
             Similarly if no digit is exceeded by the digit to its right it is called a decreasing number; for example, 66420.
             We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number; for example, 155349.
             Find the least number for which the proportion of bouncy numbers is exactly 99%.
Answer: 
Execution time: 0.0000s
"""

from utils import profiler


@profiler
def compute():
    """Calculate how many bouncy numbers there are until we have reach our percentage"""
    bouncy = 0
    total = 101

    while True:
        up, down = False, False
        lst = list(str(total))
        num = lst[0]

        # Compare each entry with the next to determine whether we are going up or down
        for next_num in lst[1:]:
            if next_num < num:
                down = True
            elif next_num > num:
                up = True

            num = next_num

        if up and down:
            bouncy += 1

        proportion = bouncy / total
        if proportion > 0.99:
            break

        total += 1

    return bouncy / total * 100


if __name__ == "__main__":
    print(f"Problem 112: {compute()}")
