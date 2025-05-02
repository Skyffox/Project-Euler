# pylint: disable=line-too-long
"""
Problem 38: Pandigital Multiples

Problem Description:
Take the number 192 and multiply it by each of 1, 2, and 3: By concatenating each product, we get the 1 to 9 pandigital number, 192384576.
We will call 192384576 the concatenated product of 192 and (1, 2, 3).
The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, giving the pandigital 918273645.
What is the largest 1 to 9 pandigital 9-digit number that can be formed as the concatenated product of an integer with (1, 2, ..., n), where n > 1?

Answer: 932718654
"""

from utils import profiler


@profiler
def compute() -> int:
    """  
    The function iterates over potential integers, concatenates their products with numbers from 1 upwards,
    and checks if the result forms a valid 9-digit pandigital number. The largest such number is returned.
    
    Returns:
        int: The largest pandigital number that can be formed by concatenating products.
    """
    biggest_outcome = 987654321 # Biggest pandigital
    outcomes = []

    for n in range(2, 20000): # Iterate over possible integers to form concatenated products
        prod = ''
        tmp = ''
        add = True

        for i in range(1, 9):
            prod += str(n * i) # Concatenate the product of n and i

            # If the concatenated product exceeds the largest pandigital number, break
            if int(prod) > biggest_outcome:
                break

            tmp = prod # Store the current concatenated product

        # Check if the concatenated product is a pandigital number
        if len(set(list(tmp))) == 9 and len(list(tmp)) == 9:
            tmp_lst = [int(x) for x in tmp]
            for i in range(1, 10):
                if i not in tmp_lst:
                    add = False
                    break

            if add:
                outcomes.append(tmp)

    # Return the largest pandigital number found
    return max([int(x) for x in outcomes])


if __name__ == "__main__":
    print(f"Problem 38: {compute()}")
