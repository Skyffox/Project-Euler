# pylint: disable=line-too-long
"""
Problem 112: Bouncy Numbers

Problem description:
A number is called an increasing number if no digit is exceeded by the digit to its left. For example, 134468 is an increasing number.
Similarly, a number is called a decreasing number if no digit is exceeded by the digit to its right. For example, 66420 is a decreasing number.
If a number is neither increasing nor decreasing, it is called a "bouncy" number. For example, 155349 is a bouncy number.

The task is to find the least number for which the proportion of bouncy numbers is exactly 99%.

Answer: 1587000
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Compute the least number for which the proportion of bouncy numbers is exactly 99%.

    A number is considered bouncy if it is neither strictly increasing nor strictly decreasing.
    This function iterates through numbers, checks if they are bouncy, and calculates the proportion
    of bouncy numbers. The process continues until the proportion of bouncy numbers exceeds 99%.

    Returns:
        int: The least number for which the proportion of bouncy numbers is exactly 99%.
    """
    bouncy = 0
    total = 101 # Start from 101 since numbers below 100 cannot be bouncy

    while True:
        up, down = False, False
        lst = list(str(total)) # Convert number to a list of digits
        num = lst[0]

        # Compare each entry with the next to determine whether we are going up or down
        for next_num in lst[1:]:
            if next_num < num:
                down = True
            elif next_num > num:
                up = True

            num = next_num

        if up and down:
            bouncy += 1 # Count as bouncy if both 'up' and 'down' flags are True

        proportion = bouncy / total
        if proportion >= 0.99: # Check if the proportion exceeds 99%
            break

        total += 1

    return total # Return the least number with 99% bouncy numbers


if __name__ == "__main__":
    print(f"Problem 112: {compute()}")
