# pylint: disable=line-too-long
"""
Problem 206: Concealed Square

Problem description:
The task is to find a unique positive integer whose square has the specific pattern "1_2_3_4_5_6_7_8_9_0", where each underscore represents a single digit.

Answer: 1389019170
"""

from utils import profiler


def is_square(n: int) -> bool:
    """
    Check whether a number is a perfect square.
    A number is a perfect square if its square root, when squared, is equal to the original number.
    
    Args:
        n (int): The number to check.
    
    Returns:
        bool: True if n is a perfect square, False otherwise.
    """
    return int(n**0.5)**2 == n


def create_num(insertions: int) -> int:
    """
    Generate a number where digits are inserted into the template "1_2_3_4_5_6_7_8_9_0".
    
    This function takes a number (insertions), converts it to a string, and inserts each digit of
    the number into the underscores of the template at the correct positions.
    
    Args:
        insertions (int): The number whose digits are to be inserted into the template.
    
    Returns:
        int: The newly formed number after the insertions.
    """
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    index = 1
    insertions = list(str(insertions))
    for num in insertions:
        lst.insert(index, num)
        index += 2

    return int("".join(lst))


@profiler
def compute() -> int:
    """
    Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0.
    
    This function iterates through potential candidates for the missing digits and checks
    whether the square of the generated number matches the desired pattern. The process
    continues until a number whose square fits the pattern is found.
    
    Returns:
        int: The square root of the number that produces the desired square pattern.
    """
    insert_number = 999999999 # Start from the largest number that can fit the pattern

    while insert_number > 0:
        n = create_num(insert_number)
        if is_square(n):
            break

        insert_number -= 1 # Decrease the insertion number until a match is found

    return int(n**0.5) # Return the square root of the number that generates the correct square


if __name__ == "__main__":
    print(f"Problem 206: {compute()}")
