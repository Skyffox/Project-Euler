# pylint: disable=line-too-long
"""
Problem 30: Digit Fifth Powers

Problem description:
Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

For example, the number 4150 is equal to the sum of the fifth powers of its digits:
    4^5 + 1^5 + 5^5 + 0^5 = 4150

Answer: 443839
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the sum of all numbers that can be written as the sum of the fifth powers of their digits.
    
    The function iterates over all numbers from 2 up to a specified upper limit, calculates the sum of the 
    fifth powers of the digits of each number, and checks if this sum equals the number itself.
    
    Returns:
        int: The sum of all such numbers.
    """
    # Calculate the maximum number to check, based on the sum of fifth powers of digits
    roof = 5 * 9**5
    result = 0

    # Iterate over all possible numbers
    for i in range(2, roof):
        digit_sum = 0
        number = i

        # Calculate the sum of the fifth powers of the digits
        while number > 0:
            digit = number % 10
            number //= 10
            digit_sum += digit**5

        # If the sum matches the number itself, add it to the result
        if digit_sum == i:
            result += i

    return result


if __name__ == "__main__":
    print(f"Problem 30: {compute()}")
