# pylint: disable=line-too-long
"""
Problem 55: Lychrel Numbers

Problem description:
A Lychrel number is a number that cannot form a palindrome through the iterative process of repeatedly reversing its digits and adding the 
reversed digits to the original number. For example, 196 is suspected to be a Lychrel number because it has not been shown to form a 
palindrome after many iterations. The task is to find how many Lychrel numbers exist below ten-thousand (10000).

Answer: 249
"""

from utils import profiler


def palindrome(num: int) -> bool:
    """
    Check if a number is a palindrome.
    
    Args:
        num (int): The number to check.
        
    Returns:
        bool: True if the number is a palindrome, False otherwise.
    """
    return str(num) == str(num)[::-1]


@profiler
def compute():
    """
    Computes the number of Lychrel numbers below 10,000 by checking each number for the possibility 
    of forming a palindrome within 50 iterations.
    
    Returns:
        int: The number of Lychrel numbers below 10,000.
    """
    lynchrel_nums = 0

    for n in range(10000):
        is_palindrome = False
        current_num = n

        for _ in range(51): # Up to 50 iterations
            reverse = int(str(current_num)[::-1])
            num = current_num + reverse

            if palindrome(num):
                is_palindrome = True
                break

            current_num = num

        if not is_palindrome:
            lynchrel_nums += 1

    return lynchrel_nums


if __name__ == "__main__":
    print(f"Problem 55: {compute()}")
