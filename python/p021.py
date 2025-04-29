# Let d(n) be defined as the sum of proper divisors of n (numbers less than n
# which divide evenly into n). If d(a) = b and d(b) = a, where a ≠ b, then a
# and b are an amicable pair and each of a and b are called amicable numbers.
# Evaluate the sum of all the amicable numbers under 10000.
# Execution time: 3.468s

def proper_divisors(inputs):
    counter = 0
    for number in range(1, inputs):
        if inputs % number == 0:
            counter += number
    return counter


def amicable_pairs(low, high):
    L = [proper_divisors(i) for i in range(low, high + 1)]
    pairs = []

    for i in range(high - low + 1):
        index = L[i]
        if high >= index > i + low == L[index - low] and low <= index:
            pairs.append([i + low, index])
    return pairs


def sum_pairs(pairs):
    return sum([sum(pair) for pair in pairs])


print("Number of amicable pairs under 10000: " + str(sum_pairs(amicable_pairs(1, 10000))))
if __name__ == "__main__":
    print(f"Problem 1: {compute()}")
