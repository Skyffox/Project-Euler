# Find the value of D ≤ 1000 in minimal solutions of x for which the largest value of x is obtained.
# Equation: x^2 - Dy^2 = 1
# Execution time: ???


# The following is the algorithm for solving “Pell's equation”, x2 – Ny2 = 1, as given by the Indian mathematicians who were the first to solve this equation:

# For the given value of N (which is not a perfect square) replace x by a, y by b and 1 by k and solve the equation a2 – Nb2 = k. Let the initial value of b be 1 and select the initial value of a such that the square of the number is as close to N as possible so as to get the least absolute value of k. Note that k may be either positive or negative but not zero.
# Now select an integer m such that k divides a + bm and the absolute value of m2 – N is minimum.
# Now replace a by the absolute value of (am + Nb)/k and b by the absolute value of (a + bm)/k.
# Now replace k by a2 – Nb2. Note that k may be either positive or negative but not zero.
# If the new value of k is 1 we have got the solution. The value of x is a and that of y is b.
# If the value of k is not equal to 1 we go for the first iteration and repeat steps 1 to 5. We keep on doing this until the value of k becomes 1 and we thus get the values of x and y which satisfies “Pell's equation” for the given value of N.
# Using Brahmagupta's lemma, if the value of k assumes a value of -1 or ± 2 for any value of a and b or if the value of k assumes a value of ± 4 and either a or b is an even number, we can stop further iterations and compose the triple with itself to get the final solution.
# a2 – Nb2 = k     ==>     {(a2 + Nb2)/k}2 – N{(ab)/k}2 = 1


# Pell's Equation Background:
# The equation 
# 𝑥
# 2
# −
# 𝐷
# 𝑦
# 2
# =
# 1
# x 
# 2
#  −Dy 
# 2
#  =1 is known as Pell's equation. The solutions 
# 𝑥
# x and 
# 𝑦
# y are positive integers, and the smallest solution 
# (
# 𝑥
# 1
# ,
# 𝑦
# 1
# )
# (x 
# 1
# ​
#  ,y 
# 1
# ​
#  ) can be found using continued fractions to approximate the square root of 
# 𝐷
# D. Once we find the smallest solution, larger solutions can be generated iteratively.


import math

# Function to check if a number is a perfect square
def is_perfect_square(n):
    return int(math.isqrt(n))**2 == n

# Function to solve Pell's equation for a given D
def solve_pells_equation(D):
    m, d, a = 0, 1, int(math.isqrt(D))
    if a * a == D:
        return None  # No solution if D is a perfect square
    num1, num2 = 1, a
    denom1, denom2 = 0, 1
    while num2 * num2 - D * denom2 * denom2 != 1:
        m = d * a - m
        d = (D - m * m) // d
        a = (int(math.isqrt(D)) + m) // d
        num1, num2 = num2, a * num2 + num1
        denom1, denom2 = denom2, a * denom2 + denom1
    return num2  # Return the minimal x

# Find the value of D for which the equation has the largest x
def find_max_x(limit):
    max_x = 0
    best_d = 0
    for D in range(2, limit + 1):
        if not is_perfect_square(D):
            x = solve_pells_equation(D)
            if x and x > max_x:
                max_x = x
                best_d = D
    return best_d

# Set the limit (D <= 1000)
limit = 1000

# Get the result
result = find_max_x(limit)
print(result)

if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
