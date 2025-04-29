# Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.
# Execution time: 17.000s

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


def sieve(n):
    """
    We cross out all composites from 2 to sqrt(N)
    """
    p = [1] * n
    p[0] = 0
    p[1] = 0

    i = 2
    # This will loop from 2 to int(sqrt(x))
    while i*i <= n:
        # If we already crossed out this number, then continue
        if p[i] == 0:
            i += 1
            continue

        j = 2*i
        while j < n:
            # Cross out this as it is composite
            p[j] = 0
            # j is incremented by i, because we want to cover all multiples of i
            j += i

        i += 1
                
    return p


# Set roof to which primes we want.
ones = sieve(8500)
primes = [i for i, x in enumerate(ones) if x == 1]

ans = 0
# Set stop condition.
b = False

# Loop over all primes numbers and set starting positions for each new loop.
# Then add the numbers together check if still prime. Do this for every stage.
for i, first in enumerate(primes[:-4]):
    for j, second in enumerate(primes[i+1:]):
        if is_prime(int(str(first) + str(second))) and is_prime(int(str(second) + str(first))):

            for k, third in enumerate(primes[i+j+2:]):
                if is_prime(int(str(first) + str(third))) and is_prime(int(str(second) + str(third))) and \
                   is_prime(int(str(third) + str(first))) and is_prime(int(str(third) + str(second))):

                    for l, fourth in enumerate(primes[i+j+k+3:]):
                        if is_prime(int(str(first) + str(fourth))) and is_prime(int(str(second) + str(fourth))) and \
                           is_prime(int(str(third) + str(fourth))) and is_prime(int(str(fourth) + str(first))) and \
                           is_prime(int(str(fourth) + str(second))) and is_prime(int(str(fourth) + str(third))):

                            for fifth in primes[i+j+k+l+4:]:
                                if is_prime(int(str(first) + str(fifth))) and is_prime(int(str(second) + str(fifth))) and \
                                   is_prime(int(str(third) + str(fifth))) and is_prime(int(str(fourth) + str(fifth))) and \
                                   is_prime(int(str(fifth) + str(first))) and is_prime(int(str(fifth) + str(second))) and \
                                   is_prime(int(str(fifth) + str(third))) and is_prime(int(str(fifth) + str(fourth))):

                                    b = True
                                    ans = first + second + third + fourth + fifth
                            if b:
                                break
                    if b:
                        break
            if b:
                break
    if b:
        break


print("Lowest sum for a set of five primes:", ans)


if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
