# By replacing the 1st digit of the 2-digit number *3, it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.
# By replacing the 3rd and 4th digits of 56**3 with the same digit, this 5-digit number is the first example having seven primes among the ten generated numbers, 
# yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003, being the first member of this family, is the smallest prime with this property.
# Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
# Execution time: 1.755s

from helper import sieve_of_atkin

def is_prime(n):
    """
    Assumes that n is a positive natural number
    """
    # We know 1 is not a prime number
    if n == 1:
        return False

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # Check if i divides x without leaving a remainder
        if n % i == 0:
            # This means that n has a factor in between 2 and sqrt(n)
            # So it is not a prime number
            return False
        i += 1
    # If we did not find any factor in the above loop,
    # then n is a prime number
    return True


primes_lst, bool_sieve = sieve_of_atkin(125000)

# Go look if you can find more primes.
for num in primes_lst:
    num = str(num)

    for i in range(0, 10):
        c = 1
        i = str(i)
        if i not in num:
            continue

        for j in range(1, 10):
            j = str(j)
            if i == j:
                continue

            copy_num = num.replace(i, j)
            n = int(copy_num)

            if (n < 125000 and bool_sieve[n]) or is_prime(n):
                c += 1

            if c == 8:
                print("Smallest prime:", num)
                break

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
