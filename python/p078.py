# You need to:

# Calculate the number of partitions p(n) for each n.
# Find the first n where p(n) % 1,000,000 == 0.
# To solve this, we use a recurrence relation for partition numbers, where:

# p(n)=∑k=1 n (−1)^(k−1) p(n−k(3k−1)/2)−(−1)^k p(n−k(3k+1)/2)

# The formula I used to compute the partition numbers is derived from a combinatorial identity known as Euler's Pentagonal Number Theorem.
# The partition function 𝑝(𝑛) represents the number of ways an integer 𝑛 can be written as a sum of positive integers, where the order of the addends does not matter.
# https://en.wikipedia.org/wiki/Pentagonal_number_theorem

# This function calculates the partition numbers p(n) for each n up to a specified limit. 
# The recurrence relation for partition numbers is used here. It also handles pentagonal 
# numbers as part of the recurrence and keeps the result modulo 1,000,000 to ensure we don't encounter overflow issues.
def partition_numbers(limit):
    """Return the partition numbers p(n) for all n up to the given limit."""
    p = [0] * (limit + 1)
    p[0] = 1  # Base case: there is one way to partition 0 (the empty sum)
    
    for n in range(1, limit + 1):
        total = 0
        k = 1
        while True:
            # Generalized pentagonal numbers
            pentagonal1 = k * (3 * k - 1) // 2
            pentagonal2 = k * (3 * k + 1) // 2
            
            if pentagonal1 > n:
                break

            # Add the partitions for pentagonal numbers
            sign1 = -1 if k % 2 == 0 else 1
            total += sign1 * p[n - pentagonal1]
            
            if pentagonal2 <= n:
                sign2 = -1 if k % 2 == 0 else 1
                total += sign2 * p[n - pentagonal2]
            
            k += 1
        
        p[n] = total % 1000000  # Keep numbers mod 1,000,000 to avoid overflow
    
    return p

def compute():
    """Find the first number n for which p(n) is divisible by n_modulo."""
    limit = 100000  # Set a large limit to search for the partition number
    partitions = partition_numbers(limit)
    
    for n in range(1, limit + 1):
        if partitions[n] == 0:
            return n
    return None

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
