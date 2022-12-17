# However, in 2004 there was found a massive non-Mersenne prime which contains 2,357,207 digits: 28433×27830457+1.
# Find the last ten digits of this prime number.
# Execution time: 0.215s

print((28433 * pow(2, 7830457, 10000000000) + 1) % 10000000000)
