# pylint: disable=line-too-long
"""
Problem 59: XOR Decryption

Problem description:
In this problem, we are tasked with decrypting a cipher text that has been encrypted using XOR with a repeating key. 
The cipher text is a sequence of ASCII values, and the key is a 3-character string. The goal is to decrypt the message and 
find the sum of the ASCII values in the original text.

Answer: 129448
"""

from utils import profiler


def is_valid_character(char: str) -> bool:
    """
    Check if the provided character is valid according to a predefined set of acceptable characters.
    
    Valid characters include:
    - Lowercase and uppercase letters (a-z, A-Z)
    - Digits (0-9)
    - Whitespace, punctuation, and specific symbols: space, quotes, commas, brackets, colons, slashes, parentheses, and semicolons
    
    Args:
        char (str): A single character to be checked.
        
    Returns:
        bool: True if the character is valid, False otherwise.
    """
    acceptable_chars = set(
        'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ  ,[]"\':0123456789/().;+'
    )

    return char in acceptable_chars


@profiler
def compute() -> int:
    """
    Decrypts an XOR-encrypted message using a 3-character repeating key and calculates 
    the sum of ASCII values of the decrypted text.

    The cipher text is a sequence of ASCII values, and the goal is to try every 
    possible 3-character key to decrypt the message. The valid characters for the 
    decrypted message include uppercase and lowercase letters, digits, and some punctuation marks. 
    Once a valid decryption is found, the sum of ASCII values of the decrypted characters is calculated.

    Returns:
        int: The sum of the ASCII values of the decrypted characters.
    """
    # Open the encrypted file with ASCII characters.
    with open("inputs/p059_cipher.txt", "r", encoding="utf-8") as f:
        vals = f.read().strip().split(',')
        vals = [int(x) for x in vals]

    valid_txts = []

    # Try every key possible.
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        for j in alphabet:
            for k in alphabet:
                txt = []
                bad = False
                ascii_indices = [ord(i), ord(j), ord(k)]

                # Run the key over the file.
                for x, val in enumerate(vals):
                    char = chr(val ^ ascii_indices[x % 3])

                    # if char not in c_valid:
                    if not is_valid_character(char):
                        bad = True
                        break
                    txt.append(char)

                # If all characters are valid, store the decrypted text.
                if not bad:
                    valid_txts.append(txt)

    # Sum the ASCII values of the valid decrypted texts.
    total_sum = 0
    for text in valid_txts:
        # print(''.join(text)) # In case we want to read the text
        for letter in text:
            total_sum += ord(letter)

    return total_sum


if __name__ == "__main__":
    print(f"Problem 59: {compute()}")
