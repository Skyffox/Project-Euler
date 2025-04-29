# The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, 
# and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.
# Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
# Execution time: 2.212s

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n < 2:
        return False
    # Check only for odd numbers
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

primes = 0
sum_primes = 0
n = 8
while primes < 11:
    if not is_prime(n):
        n += 1
        continue
    
    lst = list(str(n))
    
    l = [int(''.join(lst[x:])) for x in range(1, len(lst))]
    r = [int(''.join(lst[:-x])) for x in range(1, len(lst))]
    
    if all(is_prime(num) for num in l) and all(is_prime(num) for num in r):
        primes += 1
        sum_primes += n

    n += 1
    
print ("Sum of eleven truncatable primes:", sum_primes)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
