# Find the largest palindrome made from the product of two 3-digit numbers.
# Execution time: 0.259s

def is_palindrome(n):
    n = str(n)
    return n == n[::-1]


def largest_palindrome():
    thirdnumber = 0
    for number in range(100, 1000):
        for secondnumber in range(number, 1000):
            product = number * secondnumber

            if product <= thirdnumber:
                continue

            if is_palindrome(product):
                thirdnumber = product

    print(thirdnumber)


largest_palindrome()
