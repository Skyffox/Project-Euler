# pylint: disable=line-too-long
"""
Problem 89: Roman Numerals

Problem description:
This module solves how many characters can be saved by converting Roman numerals in a given list to their minimal 
form. The input is a list of Roman numerals, and the output is the total number of characters saved by 
converting them to their minimal Roman numeral forms.

Answer: 743
"""

from utils import profiler


@profiler
def compute() -> int:
    """
    Computes the number of characters saved by converting Roman numerals
    to their minimal form. It reads a list of Roman numerals from a file,
    converts them to integer values, re-converts them to their minimal form,
    and calculates how many characters are saved.

    Returns:
        int: The total number of characters saved.
    """
    # Dictionary mapping Roman numerals to their corresponding values
    literals = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    # Mapping of integer values to Roman numerals
    roman_map = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    # Convert a Roman numeral string to an integer
    def roman_to_int(roman: str) -> int:
        total = 0
        prev_value = 0
        for char in reversed(roman):
            value = literals[char]
            if value < prev_value:
                total -= value # Subtraction rule (IV, IX, etc.)
            else:
                total += value
            prev_value = value
        return total

    # Convert an integer to its minimal Roman numeral form
    def int_to_roman(num: int) -> str:
        roman = ""
        for value, symbol in roman_map:
            while num >= value:
                roman += symbol
                num -= value
        return roman

    # Read the file and process the Roman numerals
    with open('inputs/p089_roman.txt', 'r', encoding="utf-8") as f:
        total_saved = 0
        for line in f:
            line = line.strip()

            # Get the original length of the Roman numeral
            original_length = len(line)

            # Convert the Roman numeral to an integer
            integer_value = roman_to_int(line)

            # Convert the integer back to its minimal Roman numeral form
            minimal_roman = int_to_roman(integer_value)

            # Count the number of characters saved
            total_saved += (original_length - len(minimal_roman))

    return total_saved


if __name__ == "__main__":
    print(f"Problem 89: {compute()}")
