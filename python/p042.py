# pylint: disable=line-too-long
"""
Problem: Coded Triangle Numbers

Problem Description:
By converting each letter in a word to a number corresponding to its alphabetical position (A = 1, B = 2, ..., Z = 26), 
and summing these values, we obtain a word value. For example, the word value of "SKY" is 19 + 11 + 25 = 55.

If the word value is a triangle number, the word is considered a "triangle word."

The task is to find how many triangle words are present in a given list of words.

Answer: 162
"""

import math
from utils import profiler


def is_triangle_number(word_value: int) -> bool:
    """
    Checks if a given word value is a triangle number.
    
    A triangle number is of the form n(n+1)/2. We check if the value corresponds to such a number 
    by solving the quadratic equation n^2 + n - 2 * word_value = 0. If the discriminant of the 
    quadratic equation is a perfect square, the word value is a triangle number.
    
    Args:
        word_value (int): The sum of the alphabetical values of the word's letters.
        
    Returns:
        bool: True if the word value is a triangle number, otherwise False.
    """
    discriminant = 1 + 8 * word_value
    if discriminant > 0:
        sqrt_discriminant = math.isqrt(discriminant)
        return sqrt_discriminant * sqrt_discriminant == discriminant
    return False


def letter_to_value(letter: str) -> int:
    """
    Converts a letter to its corresponding alphabetical position value (A = 1, B = 2, ..., Z = 26).
    
    Args:
        letter (str): A single uppercase letter.
        
    Returns:
        int: The alphabetical value of the letter (1 for A, 2 for B, ..., 26 for Z).
    """
    return ord(letter) - ord('A') + 1


@profiler
def compute() -> int:
    """
    Counts the number of triangle words in a given file.
    
    The file is expected to contain a list of words separated by commas. Each word is evaluated 
    by summing the alphabetical positions of its letters, and checking if the sum is a triangle number.
    
    Args:
        filename (str): The path to the file containing the list of words.
        
    Returns:
        int: The number of triangle words found in the file.
    """
    triangle_words = 0

    with open("inputs/p042_words.txt", "r", encoding="utf-8") as f:
        words = f.read().replace('"', '').split(',')

        for word in words:
            # Calculate word value
            word_value = sum(letter_to_value(letter) for letter in word)

            # Check if the word value is a triangle number
            if is_triangle_number(word_value):
                triangle_words += 1

    return triangle_words


if __name__ == "__main__":
    print(f"Problem 42: {compute()}")
