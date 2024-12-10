# How many continued fractions for N ≤ 10000 have an odd period?
# Execution time: 0.662s

# https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion

odd_periods = 0

for root in range(2, 10000):
    m_n = 0
    d_n = 1
    a0 = int(root**0.5)

    if a0 * a0 == root:
        continue

    a_n = a0
    triplets = []
    period = []

    while True:
        m_n = d_n * a_n - m_n
        d_n = (root - m_n**2) / d_n

        a_n = int((a0 + m_n) / d_n)

        if [m_n, d_n, a_n] in triplets:
            break

        triplets.append([m_n, d_n, a_n])
        period.append(a_n)

    if len(period) % 2 != 0:
        odd_periods += 1

print(odd_periods)
