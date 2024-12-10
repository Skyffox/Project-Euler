# In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?
# Execution time: 0.269s

c = 0

# Starting values of numerator and denominator.
above = 3
below = 2

for i in range(1000):
    num = above / below

    # Calculate new values.
    tmp = above
    above = above + 2 * below
    below = tmp + below

    # Check which list is longer.
    lst_above = [int(x) for x in str(above)]
    lst_below = [int(x) for x in str(below)]

    if len(lst_above) > len(lst_below):
        c += 1

print("Amount of time numerator was greater than denominator:", c)



