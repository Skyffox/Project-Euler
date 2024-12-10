# A perfect number is a number for which the sum of its proper divisors is
# exactly equal to the number. For example, the sum of the proper divisors of
# 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

# A number n is called deficient if the sum of its proper divisors is less than
# n and it is called abundant if this sum exceeds n.

# As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
# number that can be written as the sum of two abundant numbers is 24. By
# mathematical analysis, it can be shown that all integers greater than 28123
# can be written as the sum of two abundant numbers. However, this upper limit
# cannot be reduced any further by analysis even though it is known that the
# greatest number that cannot be expressed as the sum of two abundant numbers
# is less than this limit.

# Find the sum of all the positive integers which cannot be written as the sum
# of two abundant numbers.
# Execution time: 7.764s

def get_sum_of_divs(n):
    i = 2
    upper = n
    total = 1
    while i < upper:
        if n % i == 0:
            upper = n / i
            total += upper
            if upper != i:
                total += i
        i += 1
    return total


def is_abundant(n):
    return get_sum_of_divs(n) > n


lAbundants = [x for x in range(12, 28123) if is_abundant(x) == True]
dAbundants = {x: x for x in lAbundants}

sums = 1
for i in range(2, 28123):
    boo = True
    for k in lAbundants:
        if k < i:
            if (i - k) in dAbundants:
                boo = False
                break
        else:
            break

    if boo:
        sums += i

print(sums)
