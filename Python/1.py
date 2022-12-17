# Find the sum of all the multiples of 3 or 5 below 1000.
# Execution time: 0.213s

def sum_of_multiples(m_range):
    c = 0
    for number in range(1, m_range):
        if number % 3 == 0 or number % 5 == 0:
            c += number

    return c


print(sum_of_multiples(1000))
