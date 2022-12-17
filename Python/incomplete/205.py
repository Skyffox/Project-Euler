# What is the probability that Pyramidal Pete beats Cubic Colin? Give your answer rounded to seven decimal places in the form 0.abcdefg
# Execution time: ???

import random

it = 0
max_it = 100000000
wins = 0

while it < max_it:
    peter = random.randrange(1, 5)
    colin = random.randrange(1, 7)

    if peter > colin:
        wins += 1

    it += 1

prob = wins / it
print("win percentage of peter %.7f" %prob)
