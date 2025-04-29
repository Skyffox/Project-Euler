# pylint: disable=line-too-long
"""
Problem 19: Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
            where each “_” is a single digit.
Answer: 
Execution time: 0.0000s
"""

from utils import profiler


def is_square(n):
    """Check whether a number is a squared number"""
    return int(n**0.5)**2 == n


def create_num(insertions):
    """Insert a number into the list below"""
    lst = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    index = 1
    insertions = list(str(insertions))
    for num in insertions:
        lst.insert(index, num)
        index += 2

    return int("".join(lst))


@profiler
def compute():
    """Create an iterator of what we may insert into our number, insert this iterator into the number and check whether it is a square number"""
    insert_number = 999999999

    while insert_number > 0:
        n = create_num(insert_number)
        if is_square(n):
            break

        insert_number -= 1

    return n**0.5


if __name__ == "__main__":
    print(f"Problem 206: {compute()}")
