# The prime 41, can be written as the sum of six consecutive primes: 41 = 2 + 3 + 5 + 7 + 11 + 13
# This is the longest sum of consecutive primes that adds to a prime below one-hundred.
# The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.
# Which prime, below one-million, can be written as the sum of the most consecutive primes?
# Execution time: 0.216s


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

primes = []
s = 0
n = 2
while True:
    if is_prime(n):
        s += n
        if s < 1000000:
            primes.append(n)
        else:
            break
    n += 1

len_pri = len(primes)
for x in range(len_pri):
    # Take x primes from the left
    l = primes[:-x]
    # Take x primes from the right
    r = primes[x:]
    
    if is_prime(sum(l)):
        longest_sum = sum(l)
        terms = len(l)
        break
        
    if is_prime(sum(r)):
        longest_sum = sum(r)
        terms = len(r)
        break

print(longest_sum, terms)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
