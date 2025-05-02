# pylint: disable=line-too-long
"""
Problem 17: Number Letter Counts

Problem description:
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

Answer: 21124
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Change numbers to their letter form and calculate how many letters are used for numbers 1 through 1000.

    This function converts the numbers from 1 to 1000 into their English word forms and counts 
    the total number of letters used (excluding spaces and hyphens). The conversion takes into 
    account the ones, teens, tens, and hundreds, as well as the special case for 1000 ("onethousand").

    Returns:
        int: The total number of letters used in the word forms of the numbers from 1 to 1000.
    """
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    def count_letters(n: int) -> int:
        """
        Count the number of letters for a given number from 1 to 999.

        This function handles different ranges of numbers, from 1 to 9, 10 to 19 (teens), 
        multiples of ten (20, 30, ..., 90), and numbers in the hundreds.

        Args:
            n (int): The number to convert and count the letters for.

        Returns:
            int: The number of letters in the word form of the number.
        """
        if n == 1000:
            return len("onethousand")
        elif n >= 100:
            hundred_part = ones[n // 100] + "hundred"
            # If remainder exists, add "and" and recurse on the remainder
            return len(hundred_part) + (3 if n % 100 != 0 else 0) + count_letters(n % 100)
        elif n >= 20:
            return len(tens[n // 10] + ones[n % 10])
        elif n >= 10:
            return len(teens[n - 10])
        else:
            return len(ones[n])

    # Sum up the letter counts for numbers 1 through 1000
    total = sum(count_letters(i) for i in range(1, 1001))

    return total


if __name__ == "__main__":
    print(f"Problem 17: {compute()}")
