# Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
# Execution time: 0.445s

longest_cycle = 0
max_d = 0

# From example we know 7 is the longest
for d in range(7, 1001):
    # Find the longest cycle
    value = 10 % d
    cycle = 0
    # Maximum length of the repetent
    limit = 1000

    while value != 1 and limit > 1:
        value *= 10
        value %= d
        cycle += 1
        limit -= 1

    if cycle > longest_cycle and limit > 1:
        longest_cycle = cycle
        max_d = d

print ("The d with the longest recurring cycle:", max_d)
