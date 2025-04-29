# Given that L is the length of the wire, for how many values of L ≤ 1,500,000 can exactly one integer sided right angle triangle be formed?
# Execution time: 1.128s

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a % b
    return a


BOUND = 1500000
LIMIT = int((BOUND / 2)**0.5) # performance increase!
triangles = [0 for _ in range(BOUND + 1 )]
result = 0

for m in range(2, LIMIT):
    for n in range(1, m):
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            p = a+b+c
            while (p <= 1500000):
                if triangles[p] == 0:
                    triangles[p] = 1
                    result += 1
                elif triangles[p] == 1:
                    triangles[p] = 2
                    result -= 1

                p += a+b+c

print("Triangles with a right angle:", result)
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
