# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
# Execution time: 0.683s

def is_palindrome(n):
    return str(n) == str(n)[::-1]

potential = []
total = 0
for x in range(1, 1000000):
    if is_palindrome(x):
        potential.append(x)
        
for y in potential:
    binary_lst = list(bin(y))[2:]
    binary_n = int(''.join(binary_lst))
    if is_palindrome(binary_n):
        total += y
        
print ("Sum of double-base palindromes:", total)
    
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
