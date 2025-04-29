import math

# Function to count the fractions between 1/3 and 1/2
def count_fractions(limit):
    count = 0
    for b in range(2, limit + 1):
        # Find the range for a (where a/b is between 1/3 and 1/2)
        lower_bound = b // 3 + 1
        upper_bound = b // 2
        # Count the numbers a in this range where gcd(a, b) = 1
        for a in range(lower_bound, upper_bound + 1):
            if math.gcd(a, b) == 1:
                count += 1
    return count

# Set the limit (denominator <= 12,000)
limit = 12000

# Get the result
result = count_fractions(limit)
print(result)

#7295372

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")



# Iterating over Denominators (b): We loop over all possible denominators b from 2 to 12,000.
# Finding Numerators (a): For each b, the numerators a should satisfy 
# 𝑏
# 3
# <
# 𝑎
# <
# 𝑏
# 2
# 3
# b
# ​
#  <a< 
# 2
# b
# ​
#  . This is achieved by setting the bounds for a:
# lower_bound = b // 3 + 1
# upper_bound = b // 2
# Coprime Check: For each potential a, we check if 
# gcd
# (
# 𝑎
# ,
# 𝑏
# )
# =
# 1
# gcd(a,b)=1, ensuring the fraction is in its simplest form.
# Counting Valid Fractions: We increment the counter every time we find a valid fraction.